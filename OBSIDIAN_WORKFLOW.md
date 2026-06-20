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
  post-slug_caption-title_photo.jpg
  post-slug_caption-title_graph.png
  post-slug_caption-title_review.jpg
```

Use source image filenames in the format `post-title_full-caption-title_media-type.ext`, with lowercase kebab case in each segment. Valid media types are `image`, `graph`, `painting`, `photo`, and `review`. Use `review` for book, album, and movie collateral; review images share the same post-body dimensions.

Set `cover.image` to the descriptive cover image filename. Static `/images/...` paths still work, but page bundles or `assets/images/` are preferred for optimized output.

## Required Frontmatter

```yaml
---
title: "Post Title"
date: 2026-06-08
draft: false
type: essay
description: ""
cover:
  image: "post-title_city-country-photo_photo.jpg"
  alt: "Short description"
  caption: "City, Country - photo"
---
```

Use `type: essay`, `type: story`, or `type: note`. Essays and stories start with Roman headings like `## **I.** ***First***`; notes can start directly.

## Figures

```md
![Alt text](post-title_source-name-2026-note-short-caption_graph.png)

*Source: Source name (year). Note: short caption.*
```

Review images for books, albums, and movies use the Markdown title `"review"`:

```md
![Book cover alt text](post-title_name-year-artist_review.jpg "review")

*Name (year), Artist.*
```

Keep captions short. Do not use `***` or horizontal rules as dividers.
