# DexterBosley.com Obsidian Workflow

This site is powered by markdown files in the Hugo repo. The Obsidian vault folder `dexterbosley.com/` is an editing doorway into those real files.

## Where To Edit

- Essays: `dexterbosley.com/posts/essays/`
- Stories: `dexterbosley.com/posts/stories/`
- Notes: `dexterbosley.com/posts/notes/`
- Essay starter: `dexterbosley.com/templates/essay.md`
- Story starter: `dexterbosley.com/templates/story.md`
- Note starter: `dexterbosley.com/templates/note.md`
- Bundle starters:
  - `dexterbosley.com/templates/essay-bundle/index.md`
  - `dexterbosley.com/templates/story-bundle/index.md`
  - `dexterbosley.com/templates/note-bundle/index.md`
- Design rules: `dexterbosley.com/design-system.md`

Those folders are symlinks into `/Users/dexterbosley/projects/dexterbosley.com`, so edits made in Obsidian are edits to the live site source. New markdown files created in `posts/essays/`, `posts/stories/`, or `posts/notes/` also land in the real Hugo content folders.

## Publish Command

From Terminal:

```sh
cd /Users/dexterbosley/projects/dexterbosley.com
./publish.sh "Update journal"
```

That command rebuilds the `docs/` folder, commits everything, and pushes to GitHub Pages.


## Article Layout Rules

- Click-in essays, stories, and notes use a quiet article layout with a desktop metadata rail for date, `<- BACK`, and `^ SHARE`.
- Mobile keeps those utilities as a compact left-aligned stack below the title and theme toggle.
- Do not add progress bars, sticky reader headers, toast interactions, or standard quote blocks.
- Keep figures Markdown-only: image line, blank line, italic caption line.

## Caption Rules

- Location/photo/painting: `City/Place, Country - photo` or `City/Place, Country - painting`
- Artwork/book/album cover: `Name (year), Artist`
- Graph/screenshot/report: `Source: Source name (year). Note: short context.`

## Bundle Convention

Use a folder bundle when a post has local images:

```text
posts/essays/post-slug/
  index.md
  banner.jpg
  figure-01.png
  figure-02.jpg
  book-cover-01.jpg
  album-cover-01.jpg
```

- `index.md` is the post.
- `banner.jpg` is the required top/share image and is referenced as `cover.image: "banner.jpg"`.
- `figure-01.*`, `figure-02.*` are centered inline figures, screenshots, or graphs.
- `book-cover-01.*` and `album-cover-01.*` are for notes or essays that reference covers.
- Local bundle images can be referenced by filename; `/images/...` static paths still work.
- Share previews use the cover image automatically, including bundle-local `banner.jpg`.
- To publish: set `draft: false`, save, then run the publish command above.

Fast Obsidian flow:

1. Copy the matching bundle starter folder into `posts/essays/`, `posts/stories/`, or `posts/notes/`.
2. Rename the copied folder to the final post slug, like `my-new-essay`.
3. Put the banner image in the folder as `banner.jpg` or `banner.png`.
4. Add optional local images as `figure-01.png`, `book-cover-01.jpg`, or `album-cover-01.jpg`.
5. Edit `index.md`: title, date, `description`, cover alt/caption, and body.
6. Set `draft: false`.
7. Run the publish command.

## Essay Shape

```yaml
---
title: "Essay Title"
date: 2026-03-30
draft: false
type: essay
description: ""
cover:
  image: "banner.jpg"
  alt: "Short description of the banner image"
  caption: "City/Place, Country - photo"
---
```

Essays start after the required banner with Roman numeral headings and italic section titles:

```md
## **I.** ***First***

First section.

## **II.** ***Next***

Second section.
```

Use this centered figure pattern for intentional screenshots, graphs, and diagrams:

```md
![Alt text](figure-01.png)

*Source: Source name (year). Note: short descriptive caption.*
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
  image: "banner.jpg"
  alt: "Short description of the banner image"
  caption: "City/Place, Country - photo"
---
```

Stories start after the required banner pause with Roman numeral headings and italic section titles:

```md
## **I.** ***First***

Opening paragraph.

## **II.** ***Next***

Next section.
```

Use the same `## **I.** ***Section Title***` pattern for essays and stories. Do not use `***` as a story divider.

## Note Shape

```yaml
---
title: "Note Title"
date: 2026-06-08
draft: false
type: note
description: ""
cover:
  image: "banner.jpg"
  alt: "Short description of the note banner image"
  caption: "City/Place, Country - photo"
---
```

Notes are short, tweet-like entries with a small top banner. They do not need Roman numeral sections or story dividers.

## Copyable Blocks

Inline figure:

```md
![Alt text](figure-01.png)

*Source: Source name (year). Note: short descriptive caption.*
```

Publish after saving:

```sh
cd /Users/dexterbosley/projects/dexterbosley.com
./publish.sh "Update journal"
```
