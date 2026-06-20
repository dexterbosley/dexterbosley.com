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

## Newsletter And Analytics

- Subscribe page: `/subscribe/`
- Newsletter control panel: `https://newsletter.dexterbosley.com`
- Public signup form: `https://newsletter.dexterbosley.com/subscription/form`
- listmonk list: `Free Updates`
- list UUID: `853dabc3-3d14-4070-92d6-95f37ad85ae9`
- Sender: `Dexter Bosley <updates@dexterbosley.com>`
- Newsletter host: PikaPods pod `dexter-newsletter`
- Email sender: Resend, verified domain `dexterbosley.com`
- DNS provider: Squarespace
- Analytics dashboard: `https://dexterbosley.goatcounter.com`

Keep secrets out of this repo. Resend API keys, listmonk admin passwords, and PikaPods credentials should stay in their dashboards or a private password manager.

Before publishing newsletter or tracking changes:

1. Run `hugo --cleanDestinationDir`.
2. Confirm `docs/subscribe/index.html` exists.
3. Confirm generated pages include `https://dexterbosley.goatcounter.com/count`.
4. Open `https://newsletter.dexterbosley.com/subscription/form` and confirm the public form loads.
5. For end-to-end signup checks, submit a test address and confirm the opt-in email from `updates@dexterbosley.com`.

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
  caption: "City, Country"
---
```

Use `type: essay`, `type: story`, or `type: note`. Essays and stories start with Roman headings like `## **I.** ***First***`; notes can start directly. Notes still require `cover` fields for metadata/share images, but do not render a visible cover banner.

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

For notes, put the review image and caption first, then body text after a blank line. Book, album, and movie review images use the fixed review treatment. Any other note image should use the same left-aligned width treatment as Home/About text, and note body text follows that same width.

Keep captions short and formal. Do not append media-type suffixes such as `- photo` or `- painting`. Do not use `***` or horizontal rules as dividers.
