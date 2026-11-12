#!/usr/bin/env python3
"""Local Markdown editor. Python 3.10+, Git; no Python packages required."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import platform
import re
import secrets
import shutil
import subprocess
import sys
import tarfile
import threading
import time
import urllib.request
import webbrowser
import zipfile
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
HUGO_VERSION = "0.157.0"
ALLOWED = ("content/", "assets/", "static/", "docs/")


def run(*args, root=ROOT, timeout=120):
    result = subprocess.run([str(a) for a in args], cwd=root, capture_output=True,
                            encoding="utf-8", errors="replace", timeout=timeout,
                            creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
    if result.returncode:
        raise ValueError((result.stderr + "\n" + result.stdout).strip() or "Command failed")
    return result.stdout


def ensure_hugo(root=ROOT):
    binary = "hugo.exe" if os.name == "nt" else "hugo"
    cached = root / ".local-editor" / "tools" / binary
    for candidate in [os.environ.get("HUGO_BIN"), str(cached), shutil.which("hugo")]:
        if candidate and Path(candidate).is_file():
            if f"v{HUGO_VERSION}" in run(candidate, "version", root=root):
                return candidate
    system = {"Windows": "windows", "Darwin": "darwin", "Linux": "linux"}.get(platform.system())
    arch = {"AMD64": "amd64", "x86_64": "amd64", "arm64": "arm64", "aarch64": "arm64"}.get(platform.machine())
    if not system or not arch:
        raise ValueError("Install Hugo 0.157.0 and set HUGO_BIN to its executable.")
    target = "darwin-universal" if system == "darwin" else f"{system}-{arch}"
    extension = "zip" if system == "windows" else "tar.gz"
    filename = f"hugo_{HUGO_VERSION}_{target}.{extension}"
    base = f"https://github.com/gohugoio/hugo/releases/download/v{HUGO_VERSION}/"
    print(f"Setting up Hugo {HUGO_VERSION} (first launch only)…", flush=True)
    with urllib.request.urlopen(base + filename, timeout=60) as response:
        archive = response.read()
    with urllib.request.urlopen(base + f"hugo_{HUGO_VERSION}_checksums.txt", timeout=60) as response:
        checksums = response.read().decode("utf-8")
    expected = next((line.split()[0] for line in checksums.splitlines()
                     if line.split()[-1].lstrip("*") == filename), None)
    if not expected or hashlib.sha256(archive).hexdigest() != expected:
        raise ValueError("Hugo download failed its checksum check. Please retry.")
    cached.parent.mkdir(parents=True, exist_ok=True)
    if extension == "zip":
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            data = bundle.read(binary)
    else:
        with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as bundle:
            data = bundle.extractfile(binary).read()
    cached.write_bytes(data)
    cached.chmod(0o755)
    return str(cached)


def revision(data):
    return hashlib.sha256(data).hexdigest()


class Editor:
    def __init__(self, root, hugo, preview_url):
        self.root, self.hugo, self.preview_url = root, hugo, preview_url
        self.local = root / ".local-editor"
        self.preview = self.local / "preview"
        self.lock = threading.Lock()
        self.routes = {}
        self.preview_error = ""

    def git(self, *args):
        return run("git", *args, root=self.root)

    def path(self, name):
        path = (self.root / "content" / name).resolve()
        if not path.is_relative_to((self.root / "content").resolve()) or path.suffix != ".md":
            raise ValueError("Choose a Markdown file inside content/.")
        return path

    def read(self, name):
        path = self.path(name)
        data = path.read_bytes()
        text = data.decode("utf-8-sig").replace("\r\n", "\n")
        return {"path": name, "text": text, "revision": revision(data),
                "preview": self.preview_url + self.routes.get(name, "/"),
                "warning": self.preview_error}

    def pages(self):
        items = []
        for path in sorted((self.root / "content").rglob("*.md")):
            text = path.read_text(encoding="utf-8-sig")
            title = re.search(r'^title:\s*[\"\']?(.*?)[\"\']?\s*$', text, re.M)
            name = path.relative_to(self.root / "content").as_posix()
            items.append({"path": name, "title": title[1] if title else path.stem,
                          "draft": bool(re.search(r"^draft:\s*true\s*$", text, re.M))})
        return items

    def changed(self):
        # Separate commands avoid parsing quoted paths or porcelain rename records.
        paths = set()
        for args in [("diff", "--name-only", "-z", "HEAD"),
                     ("ls-files", "--others", "--exclude-standard", "-z")]:
            paths.update(p for p in self.git(*args).split("\0") if p)
        return sorted(paths)

    def status(self):
        paths = self.changed()
        return {"changes": paths, "publishable": [p for p in paths if p.startswith(ALLOWED)],
                "blocked": [p for p in paths if not p.startswith(ALLOWED)]}

    def build_preview(self):
        run(self.hugo, "--destination", self.preview, "--cleanDestinationDir", "--buildDrafts",
            "--buildFuture", "--environment", "development", "--baseURL", self.preview_url + "/",
            root=self.root)
        listing = run(self.hugo, "list", "all", root=self.root)
        for row in csv.DictReader(io.StringIO(listing)):
            name = row["path"].replace("\\", "/").removeprefix("content/")
            self.routes[name] = urlsplit(row["permalink"]).path
        self.preview_error = ""

    def save(self, name, text, expected):
        path = self.path(name)
        if revision(path.read_bytes()) != expected:
            raise ValueError("This file changed in another editor. Copy your edits, then reload the file to compare.")
        # Keep exact Markdown line structure; always write UTF-8 and LF.
        text = text.replace("\r\n", "\n")
        if "\r" in text or "\x00" in text:
            raise ValueError("The file contains invalid line endings or null characters.")
        backup = self.local / "backups" / name / f"{time.time_ns()}.md"
        backup.parent.mkdir(parents=True, exist_ok=True)
        backup.write_bytes(path.read_bytes())
        temp = path.with_name(path.name + ".editor-tmp")
        try:
            temp.write_bytes(text.encode("utf-8"))
            os.replace(temp, path)
        finally:
            temp.unlink(missing_ok=True)
        result = self.read(name)
        try:
            self.build_preview()
            result = self.read(name)
        except ValueError as error:
            self.preview_error = "Saved locally, but preview could not build: " + str(error)
            result["warning"] = self.preview_error
        return result

    def create(self, title, kind):
        if kind not in {"essays", "stories", "notes"} or not title.strip():
            raise ValueError("Enter a title and choose essay, story, or note.")
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        if not slug:
            raise ValueError("Use at least one letter or number in the title.")
        name = f"{kind}/{slug}/index.md"
        path = self.path(name)
        if path.exists() or (self.root / "content" / kind / f"{slug}.md").exists():
            raise ValueError("A page with that filename already exists.")
        path.parent.mkdir(parents=True, exist_ok=True)
        text = f'''---
title: {json.dumps(title.strip(), ensure_ascii=False)}
date: {time.strftime('%Y-%m-%d')}
draft: true
description: "Add a short description."
home_recent: true
cover:
  image: "/images/placeholders/essay-story-banner-placeholder.jpg"
  alt: "Placeholder image"
  caption: "Replace with your cover and caption."
---

## **I.**

Start writing here.
'''
        path.write_bytes(text.encode("utf-8"))
        self.build_preview()
        return self.read(name)

    def sync(self):
        if self.changed():
            raise ValueError("Publish or set aside local changes before getting updates from another computer.")
        self.git("fetch", "origin", "main")
        self.git("merge", "--ff-only", "origin/main")
        self.build_preview()
        return {"message": "Latest files downloaded. Choose a page to open it."}

    def publish(self, message="Publish writing from local editor"):
        status = self.status()
        if status["blocked"]:
            raise ValueError("Other project files have changes; handle those in Git first: " + ", ".join(status["blocked"]))
        if self.git("diff", "--cached", "--name-only").strip():
            raise ValueError("Git already has staged changes. Commit or unstage those before publishing here.")
        self.git("fetch", "origin", "main")
        try:
            self.git("merge-base", "--is-ancestor", "origin/main", "HEAD")
        except ValueError:
            raise ValueError("Another computer published newer changes. Save your work and reconcile it with origin/main in Git before publishing.")
        run(self.hugo, "--cleanDestinationDir", root=self.root)
        run(sys.executable, "scripts/check_site.py", root=self.root)
        # Never git add -A: editor/tooling/config files and credentials stay out.
        self.git("add", "--", "content", "assets", "static", "docs")
        if self.git("diff", "--cached", "--name-only").strip():
            try:
                self.git("var", "GIT_AUTHOR_IDENT")
                identity = []
            except ValueError:
                identity = ["-c", "user.name=Local editor", "-c", "user.email=local-editor@localhost"]
            self.git(*identity, "commit", "-m", message)
        self.git("push", "origin", "HEAD:main")
        return {"message": "Pushed to GitHub. The live site updates when GitHub Pages finishes deploying (usually about a minute). Drafts remain unpublished.",
                "commit": self.git("rev-parse", "--short", "HEAD").strip()}


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def respond(self, payload, status=200):
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def valid_host(self):
        return self.headers.get("Host") == self.server.host

    def do_GET(self):
        if not self.valid_host():
            return self.send_error(403)
        route = urlsplit(self.path)
        if route.path == "/":
            html = (ROOT / "scripts/editor.html").read_text(encoding="utf-8")
            html = html.replace("__TOKEN__", self.server.token)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Frame-Options", "DENY")
            self.end_headers()
            return self.wfile.write(html.encode("utf-8"))
        if self.headers.get("X-Editor-Token") != self.server.token:
            return self.send_error(403)
        try:
            if route.path == "/api/pages":
                return self.respond(self.server.editor.pages())
            if route.path == "/api/file":
                return self.respond(self.server.editor.read(parse_qs(route.query)["path"][0]))
            if route.path == "/api/status":
                return self.respond(self.server.editor.status())
            self.send_error(404)
        except (ValueError, OSError, KeyError) as error:
            self.respond({"error": str(error)}, 400)

    def do_POST(self):
        if (not self.valid_host() or self.headers.get("X-Editor-Token") != self.server.token
                or self.headers.get("Origin") not in {None, "http://" + self.server.host}):
            return self.send_error(403)
        if not self.server.editor.lock.acquire(blocking=False):
            return self.respond({"error": "Another save, sync, or publish is still running."}, 409)
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 <= size <= 2_000_000:
                raise ValueError("Request too large.")
            data = json.loads(self.rfile.read(size))
            editor = self.server.editor
            if self.path == "/api/save":
                result = editor.save(data["path"], data["text"], data["revision"])
            elif self.path == "/api/create":
                result = editor.create(data["title"], data["kind"])
            elif self.path == "/api/publish":
                result = editor.publish()
            elif self.path == "/api/sync":
                result = editor.sync()
            else:
                return self.send_error(404)
            self.respond(result)
        except (ValueError, OSError, KeyError, subprocess.TimeoutExpired) as error:
            self.respond({"error": str(error)}, 400)
        finally:
            self.server.editor.lock.release()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-open", action="store_true")
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--publish", action="store_true", help="Check and publish saved files without opening the editor")
    parser.add_argument("--message", default="Publish writing from local editor")
    args = parser.parse_args()
    if not shutil.which("git"):
        raise ValueError("Install Git and reopen the editor. See WRITING.md.")
    hugo = ensure_hugo()
    if args.publish:
        print(Editor(ROOT, hugo, "").publish(args.message)["message"])
        return
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    server.host = f"127.0.0.1:{server.server_port}"
    server.token = secrets.token_hex(32)
    preview_dir = ROOT / ".local-editor/preview"
    preview = ThreadingHTTPServer(("127.0.0.1", 0),
                                 partial(SimpleHTTPRequestHandler, directory=str(preview_dir)))
    server.editor = Editor(ROOT, hugo, f"http://127.0.0.1:{preview.server_port}")
    try:
        server.editor.build_preview()
    except ValueError as error:
        # The editor must remain available to repair invalid frontmatter/Markdown.
        server.editor.preview_error = "Preview needs a correction in your files: " + str(error)
    threading.Thread(target=preview.serve_forever, daemon=True).start()
    url = "http://" + server.host
    (ROOT / ".local-editor/session.json").write_text(json.dumps({"url": url}), encoding="utf-8")
    print(f"Local editor: {url}\nKeep this process running. Ctrl+C stops it.", flush=True)
    if not args.no_open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        preview.shutdown()
        server.server_close()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Editor could not start: {error}", file=sys.stderr)
        sys.exit(1)
