"""Tests never contact the live site's Git remote."""
import json
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path
from unittest.mock import patch

import editor


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "working"
        self.root.mkdir()
        for folder in ("content", "assets", "static", "docs", "scripts"):
            (self.root / folder).mkdir()
            (self.root / folder / ".keep").touch()
        (self.root / ".gitignore").write_text(".local-editor/\n", encoding="utf-8")
        self.source = self.root / "content/about.md"
        self.source.write_bytes(b'---\ntitle: "About"\n---\n\nOriginal.\n')
        self.ed = editor.Editor(self.root, "fake-hugo", "http://127.0.0.1:1234")
        self.ed.build_preview = lambda: None
        self.ed.git("init", "-b", "main")
        self.ed.git("config", "user.name", "Editor test")
        self.ed.git("config", "user.email", "test@localhost")
        self.ed.git("add", ".")
        self.ed.git("commit", "-m", "Fixture")
        self.remote = self.base / "remote.git"
        editor.run("git", "init", "--bare", self.remote, root=self.base)
        self.ed.git("remote", "add", "origin", str(self.remote))
        self.ed.git("push", "-u", "origin", "main")

    def test_save_preserves_unicode_tables_and_backup(self):
        old = self.ed.read("about.md")
        text = '---\ntitle: "Café — 2×"\n---\n\n| Name | Value |\n| --- | --- |\n| π | 3.14 |\n'
        result = self.ed.save("about.md", text, old["revision"])
        self.assertEqual(self.source.read_bytes(), text.encode("utf-8"))
        self.assertEqual(result["text"], text)
        backups = list((self.ed.local / "backups/about.md").glob("*.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), old["text"])
        self.assertNotEqual(result["revision"], old["revision"])

    def test_external_edit_is_not_overwritten(self):
        old = self.ed.read("about.md")
        self.source.write_text("External edit", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "another editor"):
            self.ed.save("about.md", "Overwrite", old["revision"])
        self.assertEqual(self.source.read_text(), "External edit")

    def test_paths_cannot_escape_content(self):
        for name in ("../hugo.toml", "../secrets.md", str(self.base / "outside.md"), "about.html"):
            with self.assertRaises(ValueError):
                self.ed.path(name)

    def test_new_draft_and_duplicate(self):
        result = self.ed.create("A new essay", "essays")
        self.assertIn("draft: true", result["text"])
        self.assertEqual(result["path"], "essays/a-new-essay/index.md")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.ed.create("A new essay", "essays")

    def test_publish_builds_checks_and_pushes_only_after_success(self):
        self.source.write_text("Changed", encoding="utf-8")
        actual = editor.run
        commands = []

        def fake_build(*args, **kwargs):
            if str(args[0]) == "git":
                return actual(*args, **kwargs)
            commands.append(tuple(str(a) for a in args))
            if args[0] == "fake-hugo":
                (self.root / "docs/index.html").write_text("Built", encoding="utf-8")
            return ""

        before = self.ed.git("rev-parse", "origin/main")
        with patch.object(editor, "run", side_effect=fake_build):
            self.ed.publish()
        self.assertNotEqual(before, self.ed.git("rev-parse", "origin/main"))
        self.assertEqual(len(commands), 2)
        self.assertEqual(commands[1][1], "scripts/check_site.py")
        self.assertIn("Changed", self.ed.git("show", "origin/main:content/about.md"))
        self.assertEqual(self.ed.changed(), [])

    def test_failed_check_blocks_commit_and_push(self):
        self.source.write_text("Bad table", encoding="utf-8")
        actual = editor.run
        before = self.ed.git("rev-parse", "HEAD")

        def failing_check(*args, **kwargs):
            if args[0] == "git":
                return actual(*args, **kwargs)
            if "scripts/check_site.py" in args:
                raise ValueError("Unrendered Markdown table")
            return ""

        with patch.object(editor, "run", side_effect=failing_check):
            with self.assertRaisesRegex(ValueError, "Unrendered"):
                self.ed.publish()
        self.assertEqual(before, self.ed.git("rev-parse", "HEAD"))
        self.assertEqual(before, self.ed.git("rev-parse", "origin/main"))

    def test_unrelated_files_and_staged_work_block_publish(self):
        (self.root / "secret.txt").write_text("private", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Other project files"):
            self.ed.publish()
        (self.root / "secret.txt").unlink()
        self.source.write_text("Staged work", encoding="utf-8")
        self.ed.git("add", "content")
        with self.assertRaisesRegex(ValueError, "staged"):
            self.ed.publish()

    def test_another_computer_publishing_blocks_stale_push(self):
        other = self.base / "other"
        editor.run("git", "clone", self.remote, other, root=self.base)
        # Bare repository default HEAD can still be master on older Git.
        editor.run("git", "checkout", "main", root=other)
        editor.run("git", "config", "user.name", "Other", root=other)
        editor.run("git", "config", "user.email", "other@localhost", root=other)
        (other / "content/about.md").write_text("Other computer", encoding="utf-8")
        editor.run("git", "add", "content", root=other)
        editor.run("git", "commit", "-m", "Other edit", root=other)
        editor.run("git", "push", "origin", "main", root=other)
        self.source.write_text("Local edit", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Another computer"):
            self.ed.publish()

    def test_api_rejects_foreign_origin_and_missing_token(self):
        server = editor.ThreadingHTTPServer(("127.0.0.1", 0), editor.Handler)
        server.host = f"127.0.0.1:{server.server_port}"
        server.token, server.editor = "test-token", self.ed
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            url = "http://" + server.host + "/api/save"
            for headers in ({}, {"X-Editor-Token": server.token, "Origin": "https://foreign.example"}):
                request = urllib.request.Request(url, data=b"{}", headers=headers)
                with self.assertRaises(urllib.error.HTTPError) as error:
                    urllib.request.urlopen(request)
                self.assertEqual(error.exception.code, 403)
            request = urllib.request.Request("http://" + server.host + "/api/pages",
                                             headers={"X-Editor-Token": server.token})
            with urllib.request.urlopen(request) as response:
                self.assertEqual(json.load(response)[0]["title"], "About")
        finally:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
