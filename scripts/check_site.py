#!/usr/bin/env python3
"""Check built pages, links, responsive images, feeds, and asset budgets."""

import base64
import hashlib
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1] / "docs"
ORIGIN = "https://www.dexterbosley.com"


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.tags = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def local_file(url, page_url):
    target = urlsplit(urljoin(page_url, url))
    if target.netloc not in {"www.dexterbosley.com", "dexterbosley.com"}:
        return None
    path = ROOT / unquote(target.path).lstrip("/")
    return path / "index.html" if path.is_dir() else path


def check(condition, message):
    if not condition:
        raise AssertionError(message)


pages = list(ROOT.rglob("*.html"))
check(pages, "Build the site before checking it")
for path in pages:
    source = path.read_text(encoding="utf-8")
    page = Page(source)
    page_url = ORIGIN + "/" + path.relative_to(ROOT).as_posix()
    is_redirect = any(tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh"
                      for tag, attrs in page.tags)
    if not is_redirect:
        title = re.search(r"<title>(.*?)</title>", source)
        check(title and title[1] == title[1].upper(), f"Title case: {path}")
        check(len(source.encode()) < 30000, f"Page exceeds 30 KB: {path}")
        check("<style>" not in source, f"Duplicated inline stylesheet: {path}")
        check(not re.search(r"<p>\s*\|", source), f"Unrendered Markdown table: {path}")
    for tag, attrs in page.tags:
        references = [attrs[key] for key in ("src", "href") if attrs.get(key)]
        references += [candidate.strip().split()[0]
                       for candidate in attrs.get("srcset", "").split(",") if candidate.strip()]
        for reference in references:
            target = local_file(reference, page_url)
            if target is not None:
                check(target.is_file(), f"Broken local reference in {path}: {reference}")
        if attrs.get("integrity"):
            target = local_file(attrs.get("href", attrs.get("src")), page_url)
            algorithm, digest = attrs["integrity"].split("-", 1)
            actual = base64.b64encode(hashlib.new(algorithm, target.read_bytes()).digest()).decode()
            check(actual == digest, f"Asset integrity mismatch: {target}")
        if tag == "img":
            check(bool(attrs.get("alt")), f"Missing image description: {path}")
            if attrs.get("srcset"):
                check(attrs.get("width") and attrs.get("height"), f"Missing image dimensions: {path}")
        if tag == "form":
            check(attrs.get("action") == "https://newsletter.dexterbosley.com/subscription/form",
                  f"Form has no native newsletter destination: {path}")
            check(attrs.get("method") == "post", f"Form must use POST: {path}")

home = Page((ROOT / "index.html").read_text(encoding="utf-8"))
hero = next(attrs for tag, attrs in home.tags if tag == "img")
check(hero.get("loading") == "eager" and hero.get("fetchpriority") == "high", "Home photo loads late")
webp = next(attrs for tag, attrs in home.tags if tag == "source" and attrs.get("type") == "image/webp")
for candidate in webp["srcset"].split(","):
    target = local_file(candidate.strip().split()[0], ORIGIN)
    check(target.stat().st_size < 80000, f"Home photo variant exceeds 80 KB: {target}")
fonts = [attrs for tag, attrs in home.tags if tag == "link" and attrs.get("as") == "font"]
check(len(fonts) == 2 and not any("Italic" in attrs["href"] for attrs in fonts), "Unnecessary font preload")

for path in (ROOT / "css").glob("*.css"):
    for url in re.findall(r"url\(['\"]?([^)'\"]+)", path.read_text(encoding="utf-8")):
        target = local_file(url, ORIGIN + "/css/")
        check(target is None or target.is_file(), f"Missing stylesheet asset: {url}")

for path in ROOT.rglob("*.xml"):
    ET.parse(path)
feed = ET.parse(ROOT / "index.xml")
for item in feed.findall("./channel/item"):
    body = item.findtext("{http://purl.org/rss/1.0/modules/content/}encoded")
    check(body, "RSS item has no full content")
    check(not re.search(r'(?:src|href|srcset)="/', body), "RSS contains relative links")

print(f"Passed: {len(pages)} HTML pages, local links, asset integrity, feeds, forms, and loading budgets.")
