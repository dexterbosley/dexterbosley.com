#!/usr/bin/env python3
"""
Export a generated Hugo post page as email-safe HTML for listmonk.

Usage:
  python3 scripts/export_email.py notes/tatie
  python3 scripts/export_email.py --all
"""

from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin


BASE_URL = "https://www.dexterbosley.com/"
OUTPUT_DIR = Path("email")
POST_SECTIONS = {"essays", "stories", "notes"}


class Node:
    def __init__(self, tag: str | None = None, attrs: list[tuple[str, str | None]] | None = None, data: str = ""):
        self.tag = tag
        self.attrs = attrs or []
        self.data = data
        self.children: list[Node] = []

    def attr(self, name: str, default: str = "") -> str:
        for key, value in self.attrs:
            if key == name:
                return value or ""
        return default


class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("document")
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "wbr"}:
            self.stack.append(node)

    def handle_endtag(self, tag: str):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data: str):
        self.stack[-1].children.append(Node(data=data))


def parse_html(path: Path) -> Node:
    parser = Parser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.root


def class_names(node: Node) -> set[str]:
    return set(node.attr("class").split())


def find_first(node: Node, predicate) -> Node | None:
    if predicate(node):
        return node
    for child in node.children:
        found = find_first(child, predicate)
        if found:
            return found
    return None


def find_all(node: Node, predicate) -> list[Node]:
    results = []
    if predicate(node):
        results.append(node)
    for child in node.children:
        results.extend(find_all(child, predicate))
    return results


def text_content(node: Node) -> str:
    if node.tag is None:
        return node.data
    return "".join(text_content(child) for child in node.children)


def absolute_url(value: str) -> str:
    return urljoin(BASE_URL, value)


def open_tag(tag: str, attrs: dict[str, str]) -> str:
    rendered = "".join(f' {key}="{html.escape(value, quote=True)}"' for key, value in attrs.items() if value)
    return f"<{tag}{rendered}>"


def render_inline(node: Node) -> str:
    if node.tag is None:
        return html.escape(node.data)

    if node.tag == "picture":
        image = find_first(node, lambda candidate: candidate.tag == "img")
        return render_block(image) if image else ""

    if node.tag == "img":
        return render_image(node)

    if node.tag == "a":
        attrs = {
            "href": absolute_url(node.attr("href")),
            "style": "color:#080808;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:2px;",
        }
        return open_tag("a", attrs) + render_children(node) + "</a>"

    if node.tag == "mark":
        return '<span style="background:#DBE6F1;color:#080808;padding:0 3px;">' + render_children(node) + "</span>"

    if node.tag in {"strong", "b"}:
        return "<strong>" + render_children(node) + "</strong>"

    if node.tag in {"em", "i"}:
        return "<em>" + render_children(node) + "</em>"

    if node.tag == "br":
        return "<br>"

    return render_children(node)


def render_children(node: Node) -> str:
    return "".join(render_inline(child) for child in node.children)


def render_image(node: Node, *, opener: bool = False) -> str:
    classes = class_names(node)
    width = "180" if "review-image" in classes else ("700" if opener else "580")
    max_width = "180px" if "review-image" in classes else ("700px" if opener else "580px")
    height_rule = "height:270px;object-fit:cover;" if "review-image" in classes else "height:auto;"
    attrs = {
        "src": absolute_url(node.attr("src")),
        "alt": node.attr("alt"),
        "width": width,
        "style": f"display:block;width:100%;max-width:{max_width};{height_rule}margin:0 auto;border:0;",
    }
    return open_tag("img", attrs)


def child_is_image_only(node: Node) -> bool:
    meaningful = [child for child in node.children if child.tag is not None or child.data.strip()]
    return len(meaningful) == 1 and meaningful[0].tag in {"picture", "img"}


def child_is_em_only(node: Node) -> bool:
    meaningful = [child for child in node.children if child.tag is not None or child.data.strip()]
    return len(meaningful) == 1 and meaningful[0].tag == "em"


def render_block(node: Node | None) -> str:
    if node is None:
        return ""
    if node.tag is None:
        return html.escape(node.data)

    if node.tag == "picture":
        image = find_first(node, lambda candidate: candidate.tag == "img")
        return render_image(image) if image else ""

    if node.tag == "img":
        return render_image(node)

    if node.tag == "p":
        if child_is_image_only(node):
            return f'<div style="margin:34px 0 10px;">{render_children(node)}</div>'
        if child_is_em_only(node):
            return (
                '<p style="margin:0 0 28px;color:#080808;font-family:Georgia,serif;'
                'font-size:14px;line-height:1.45;">'
                f"{render_children(node)}</p>"
            )
        return (
            '<p style="margin:0 0 24px;color:#080808;font-family:Georgia,serif;'
            'font-size:17px;line-height:1.66;">'
            f"{render_children(node)}</p>"
        )

    if node.tag in {"h2", "h3", "h4"}:
        return (
            '<h2 style="margin:46px 0 8px;color:#080808;font-family:Georgia,serif;'
            'font-size:17px;font-weight:600;line-height:1.35;">'
            f"{render_children(node)}</h2>"
        )

    if node.tag in {"ul", "ol"}:
        tag = node.tag
        return (
            f'<{tag} style="margin:0 0 24px;padding-left:24px;color:#080808;'
            'font-family:Georgia,serif;font-size:17px;line-height:1.66;">'
            f"{''.join(render_block(child) for child in node.children)}</{tag}>"
        )

    if node.tag == "li":
        return f'<li style="margin:0 0 8px;">{render_children(node)}</li>'

    if node.tag == "hr":
        return '<hr style="border:0;border-top:2px solid #080808;margin:32px 0;">'

    return "".join(render_block(child) for child in node.children)


def render_opener(figure: Node | None) -> str:
    if not figure:
        return ""
    image = find_first(figure, lambda node: node.tag == "img")
    caption = find_first(figure, lambda node: node.tag == "figcaption")
    if not image:
        return ""
    caption_html = ""
    if caption and text_content(caption).strip():
        caption_html = (
            '<p style="margin:10px 0 44px;color:#777;font-family:Arial,sans-serif;'
            'font-size:13px;line-height:1.45;">'
            f"{html.escape(text_content(caption).strip())}</p>"
        )
    return f'<div style="margin:0 0 34px;">{render_image(image, opener=True)}{caption_html}</div>'


def render_email(source: Path) -> tuple[str, str]:
    root = parse_html(source)
    article = find_first(root, lambda node: node.tag == "article" and "post-single" in class_names(node))
    if not article:
        raise SystemExit(f"No post article found in {source}")

    title = text_content(find_first(article, lambda node: node.tag == "h1") or Node()).strip()
    date = text_content(find_first(article, lambda node: node.tag == "span" and node.attr("class") == "") or Node()).strip()
    if not date:
        date = text_content(find_first(article, lambda node: node.tag == "div" and "post-meta" in class_names(node)) or Node()).strip()

    canonical = find_first(root, lambda node: node.tag == "link" and node.attr("rel") == "canonical")
    permalink = canonical.attr("href") if canonical else BASE_URL

    opener = find_first(article, lambda node: node.tag == "figure" and "post-opener" in class_names(node))
    content = find_first(article, lambda node: node.tag == "div" and "post-content" in class_names(node))
    if not content:
        raise SystemExit(f"No post content found in {source}")

    content_html = "".join(render_block(child) for child in content.children)
    opener_html = render_opener(opener)
    subject = title

    document = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
</head>
<body style="margin:0;padding:0;background:#fff;color:#080808;">
  <div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;">
    {html.escape(title)} from Dexter Bosley.
  </div>
  <main style="width:100%;background:#fff;">
    <div style="max-width:700px;margin:0 auto;padding:44px 22px 48px;">
      <p style="margin:0 0 6px;color:#777;font-family:Arial,sans-serif;font-size:13px;line-height:1.4;">{html.escape(date)}</p>
      <h1 style="margin:0 0 34px;color:#080808;font-family:Georgia,serif;font-size:22px;font-weight:600;line-height:1.18;text-transform:uppercase;">{html.escape(title)}</h1>
      {opener_html}
      {content_html}
      <hr style="border:0;border-top:2px solid #080808;margin:38px 0 14px;">
      <p style="margin:0;color:#777;font-family:Arial,sans-serif;font-size:13px;line-height:1.5;">
        Read on the site: <a href="{html.escape(permalink, quote=True)}" style="color:#080808;text-decoration:underline;">{html.escape(permalink)}</a>
      </p>
      <p style="margin:12px 0 0;color:#777;font-family:Arial,sans-serif;font-size:13px;line-height:1.5;">
        <a href="{{{{ UnsubscribeURL }}}}" style="color:#080808;text-decoration:underline;">Unsubscribe</a>
      </p>
    </div>
  </main>
</body>
</html>
"""
    return subject, document


def source_for_slug(slug: str) -> Path:
    normalized = slug.strip("/")
    path = Path("docs") / normalized / "index.html"
    if not path.exists():
        raise SystemExit(f"Could not find generated post at {path}. Run hugo --cleanDestinationDir first.")
    section = normalized.split("/", 1)[0]
    if section not in POST_SECTIONS:
        raise SystemExit(f"{slug!r} is not in one of: {', '.join(sorted(POST_SECTIONS))}")
    return path


def output_for_source(source: Path) -> Path:
    relative = source.relative_to("docs").parent
    return OUTPUT_DIR / relative.with_suffix(".html")


def export_one(source: Path) -> Path:
    _, document = render_email(source)
    destination = output_for_source(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(document, encoding="utf-8")
    return destination


def post_sources() -> list[Path]:
    sources: list[Path] = []
    for section in POST_SECTIONS:
        section_dir = Path("docs") / section
        if not section_dir.exists():
            continue
        for path in sorted(section_dir.glob("*/index.html")):
            if path.parent.name.startswith("page"):
                continue
            sources.append(path)
    return sources


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Hugo post pages as listmonk-ready email HTML.")
    parser.add_argument("slug", nargs="?", help="Post slug, for example notes/tatie")
    parser.add_argument("--all", action="store_true", help="Export all generated posts")
    args = parser.parse_args()

    if args.all:
        sources = post_sources()
    elif args.slug:
        sources = [source_for_slug(args.slug)]
    else:
        parser.error("provide a post slug or --all")

    for source in sources:
        destination = export_one(source)
        print(destination)


if __name__ == "__main__":
    main()
