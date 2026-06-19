# DexterBosley.com Obsidian Workflow

This site is powered by markdown files in the Hugo repo. The Obsidian vault folder `dexterbosley.com/` is an editing doorway into those real files.

## Where To Edit

- Essays: `dexterbosley.com/posts/essays/`
- Stories: `dexterbosley.com/posts/stories/`
- Notes: `dexterbosley.com/posts/notes/`
- Essay starter: `dexterbosley.com/templates/essay.md`
- Story starter: `dexterbosley.com/templates/story.md`
- Note starter: `dexterbosley.com/templates/note.md`
- Design rules: `dexterbosley.com/design-system.md`

Those folders are symlinks into `/Users/dexterbosley/projects/dexterbosley.com`, so edits made in Obsidian are edits to the live site source. New markdown files created in `posts/essays/`, `posts/stories/`, or `posts/notes/` also land in the real Hugo content folders.

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
cover:
  image: "/images/your-banner.jpg"
  alt: "Short description of the banner image"
  caption: "Short caption for the banner"
---
```

Essays start after the optional banner with Roman numeral headings and italic section titles:

```md
## I. *First*

First section.

## II. *Next*

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
cover:
  image: "/images/your-banner.jpg"
  alt: "Short description of the banner image"
  caption: "Short caption for the banner"
---
```

Stories start after the optional banner with Roman numeral headings and italic section titles:

```md
## I. *First*

Opening paragraph.

## II. *Next*

Next section.
```

Use the same `## I. *Section Title*` pattern for essays and stories. Do not use `***` as a story divider.

## Note Shape

```yaml
---
title: "Note Title"
date: 2026-06-08
draft: false
type: note
description: ""
---
```

Notes are short blog-style entries. They do not need banners, Roman numeral sections, or story dividers.
