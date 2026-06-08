# DexterBosley.com Design System

This site is a public journal. The visual language is plain, monospaced, quiet, and intentionally document-like. Do not make it feel like a product landing page, portfolio, magazine, or theme demo.

## Core Surface

- Background is true white: `#fff`.
- Text is near-black: `#080808`.
- Font is system monospace only: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`.
- Base font size is `14px`.
- Primary page measure is `700px`.
- Main page width is `min(calc(100% - 96px), 700px)`.
- Mobile page width is `min(calc(100% - 32px), 700px)`.
- Links are visually plain until hover. Do not add blue link styling except if a future design explicitly asks for it.
- Public navigation is intentionally minimal: homepage plus click-in posts. There is no About page and no section-only browsing page.

## Homepage Template

- Top padding: `64px` desktop, `36px` mobile.
- Header contains only: `HI, I'M DEXTER BOSLEY`.
- No byline, email, nav, logo, button, or top hyperlink.
- Header title:
  - font-size `1.08rem`
  - font-weight `800`
  - uppercase
  - letter-spacing `0.02em`
  - color `#080808`
- Gap from header to intro: `126px` desktop, `84px` mobile.
- Intro:
  - max-width `620px` desktop
  - max-width `100%` mobile
  - font-size `1rem`
  - line-height `1.55`
  - paragraph margin-bottom `1.65rem`
  - margin-bottom before index `154px` desktop, `96px` mobile
- Use yellow `<mark>` highlights sparingly for one phrase per surface, not whole sentences.

## Index Rows

- The homepage index uses a date/line/title row and is sorted newest-first.
- Do not generate or link to Essays-only or Stories-only index pages.
- Row grid: date, black horizontal rule, title.
- Dates appear in the homepage index using compact uppercase format: `MAR 30, 2026`.
- Title suffix must include post kind: `(ESSAY)`, `(STORY)`, or `(NOTES)`.
- Text is uppercase with `0.04em` letter spacing.
- The black rule is `2px` high.
- On mobile, stack date, rule, and title so each post reads as a distinct list item.

## Post Templates

- Essays, stories, and notes have explicit templates:
  - `layouts/essays/single.html`
  - `layouts/stories/single.html`
  - `layouts/notes/single.html`
  - shared renderer: `layouts/partials/post-single.html`
- Post pages do not show the homepage header.
- Post canvas width matches the homepage: `min(calc(100% - 96px), 700px)` desktop and `min(calc(100% - 32px), 700px)` mobile.
- Post padding matches the homepage: `64px 0 88px` desktop and `36px 0 64px` mobile.
- Post header contains title, date, then read estimate.
- Post date format is compact uppercase: `MAR 30, 2026`.
- Read estimate is required on every click-in post and renders like `2 min`.
- Post title:
  - uppercase
  - font-size `1.08rem`
  - font-weight `800`
  - line-height `1.35`
- Post date:
  - muted `#777`
  - font-size `0.86rem`
- Gap from post header to body: `3rem`.
- Post body:
  - font-size `1rem`
  - line-height `1.55`
  - paragraph margin-bottom `1.55rem`
- Post footer actions:
  - Use a black, in-theme action row.
  - Left action is `Back` and always points to `/`.
  - Right action is `Share` and should use native share when available, otherwise copy/prompt the current post URL.
  - Do not use red for post actions.

## Essay Structure

- Essays may define `cover.image`, `cover.alt`, and `cover.caption` in frontmatter.
- If present, the cover renders between the title/date and `## I.`.
- Essay summaries are not required and should not be used as a default post primitive.
- Essays use Roman numeral section headings as the only divider system.
- Section headings should be `## I.`, `## II.`, `## III.`, and so on.
- Do not use `---`, `***`, horizontal rules, ornaments, or centered asterisks in essays.
- The stylesheet hides accidental essay `<hr>` output, but authors should still write Roman section headings.

## Story Structure

- Stories may define `cover.image`, `cover.alt`, and `cover.caption` in frontmatter.
- If present, the cover renders between the title/date and the first paragraph.
- Story quotes/epigraphs are not part of the current template.
- Story and essay banner images share the same treatment:
  - width `100%`
  - height `250px` desktop
  - height `190px` mobile
  - `object-fit: cover`
  - `object-position: center`
- Stories use centered `***` scene dividers.
- In markdown, write a divider line as `***` between scenes.
- Story dividers render as centered bold text, not horizontal lines.

## Notes Structure

- Notes are the third public post type.
- Notes live in `content/notes/`.
- Notes follow a simple blog format: title, date, read estimate, then body.
- Notes should not require banners, Roman numeral essay sections, or story scene breaks.
- Use notes for short public journal entries, working observations, and quick updates.

## Highlights

- Highlight primitive is native HTML: `<mark>highlighted phrase</mark>`.
- Highlight color is `#ffeaa3`.
- Padding is `0 0.15em`.
- Highlights should feel like a soft annotation, not a callout. Use on short phrases only.
- Hugo allows raw HTML via `[markup.goldmark.renderer] unsafe = true` for this primitive.

## Images And Captions

- Current live content should not include decorative or placeholder images.
- Essays and stories may use a banner image with caption.
- Essays should add images only when they are intentional figures, diagrams, or graphs.
- Image markdown pattern:
  - `![Alt text](/images/file.jpg)`
  - blank line
  - `*Caption text.*`
- In post pages, image paragraphs are centered.
- Essay images and graphs should not run full width by default; they use `max-width: 580px` inside the `700px` column.
- Image margin starts at `3rem` above image and `0.75rem` below.
- Captions are plain monospace, not italic visually:
  - `font-style: normal`
  - font-size `0.82em`
  - line-height `1.4`
- Keep captions short and descriptive.

## Future Post Starter Shapes

- Essay archetype includes:
  - frontmatter with optional cover fields
  - Roman numeral headings
  - body text with optional `<mark>`
  - image and caption pattern
- Story archetype includes:
  - frontmatter with optional cover fields
  - opening paragraph
  - scene break using `***`
  - next scene
- Note archetype includes:
  - minimal frontmatter
  - short body text

## What Not To Add

- No cards.
- No rounded UI.
- No hero image.
- No decorative gradients.
- No nav unless explicitly requested.
- No email/byline under the homepage title unless explicitly requested.
- No external fonts.
- No complex JavaScript for reading behavior.

## Obsidian Editing Workflow

- The active vault is `/Users/dexterbosley/Desktop/dexter-ai/`.
- The vault contains a `dexterbosley.com/` folder with symlinked markdown folders to the real Hugo source.
- Edit or create posts in:
  - `dexterbosley.com/posts/essays/`
  - `dexterbosley.com/posts/stories/`
  - `dexterbosley.com/posts/notes/`
- Use starter shapes in:
  - `dexterbosley.com/templates/essay.md`
  - `dexterbosley.com/templates/story.md`
  - `dexterbosley.com/templates/note.md`
- Publish from Terminal:
  - `cd /Users/dexterbosley/projects/dexterbosley.com`
  - `./publish.sh "Update journal"`
- Publishing rebuilds `docs/`, commits all site changes, and pushes to GitHub Pages.
