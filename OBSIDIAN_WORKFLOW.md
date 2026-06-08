# DexterBosley.com Obsidian Workflow

This site is powered by markdown files in the Hugo repo. The Obsidian vault folder `dexterbosley.com/` is an editing doorway into those real files.

## Where To Edit

- Essays: `dexterbosley.com/posts/essays/`
- Stories: `dexterbosley.com/posts/stories/`
- Essay starter: `dexterbosley.com/templates/essay.md`
- Story starter: `dexterbosley.com/templates/story.md`
- Design rules: `dexterbosley.com/design-system.md`

Those folders are symlinks into `/Users/dexterbosley/projects/dexterbosley.com`, so edits made in Obsidian are edits to the live site source. New markdown files created in `posts/essays/` or `posts/stories/` also land in the real Hugo content folders.

## Publish Command

From Terminal:

```sh
cd /Users/dexterbosley/projects/dexterbosley.com
./publish.sh "Update journal"
```

That command rebuilds the `docs/` folder, commits everything, and pushes to GitHub Pages.

## Essay Shape

```yaml
---
title: "Essay Title"
date: 2026-03-30
draft: false
type: essay
description: ""
summary_title: "This essay discusses:"
summary_items:
  - "first thing this essay helps clarify"
  - "second thing this essay helps clarify"
  - "third thing this essay helps clarify"
---
```

Essays start after the summary with Roman numeral headings:

```md
## I.

First section.

## II.

Second section.
```

Use `<mark>highlighted phrase</mark>` only for short yellow annotations inside the essay. Do not use `***` or horizontal rules in essays.

## Story Shape

```yaml
---
title: "Story Title"
date: 2026-01-24
draft: false
type: story
description: ""
quote: "Short epigraph or line that frames the story."
quote_author: "Author Name"
cover:
  image: "/images/your-banner.jpg"
  alt: "Short description of the banner image"
  caption: "Short caption for the banner"
---
```

Stories start after the banner and quote:

```md
Opening paragraph.

***

Next scene.
```

Use `***` only for story scene breaks.
