# DexterBosley.com Obsidian Workflow

The Obsidian folder `dexterbosley.com/` is a doorway into the real Hugo repo at `/Users/dexterbosley/projects/dexterbosley.com`. Edits there are live source edits.

## Edit Here

- Essays: `dexterbosley.com/posts/essays/`
- Stories: `dexterbosley.com/posts/stories/`
- Notes: `dexterbosley.com/posts/notes/`
- Starters: `dexterbosley.com/templates/`
- Design rules: `dexterbosley.com/design-system.md`

## Preview And Publish

From `/Users/dexterbosley/projects/dexterbosley.com`:

```sh
hugo server -D
hugo --cleanDestinationDir
./publish.sh "Update journal"
```

Only publish when Dexter explicitly asks. Publishing rebuilds `docs/`, commits, and pushes to GitHub Pages.

## Post Bundles

Use a bundle when a post has local images:

```text
posts/essays/post-slug/
  index.md
  banner.jpg
  figure-01.png
```

Set `cover.image: "banner.jpg"`. Static `/images/...` paths still work, but page bundles or `assets/images/` are preferred for optimized output.

## Required Frontmatter

```yaml
---
title: "Post Title"
date: 2026-06-08
draft: false
type: essay
description: ""
cover:
  image: "banner.jpg"
  alt: "Short description"
  caption: "City, Country - photo"
---
```

Use `type: essay`, `type: story`, or `type: note`. Essays and stories start with Roman headings like `## **I.** ***First***`; notes can start directly.

## Figures

```md
![Alt text](figure-01.png)

*Source: Source name (year). Note: short caption.*
```

Keep captions short. Do not use `***` or horizontal rules as dividers.
