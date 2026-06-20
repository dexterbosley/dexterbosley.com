# DexterBosley.com Design System

This site is a public journal. The visual language is plain, quiet, editorial, and intentionally document-like. It can borrow typographic restraint from newspaper sites such as the Financial Times, but it must not copy or embed proprietary typefaces. Do not make it feel like a product landing page, portfolio, magazine, or theme demo.

## Core Surface

- Light mode background is true white: `#fff`.
- Light mode text is near-black: `#080808`.
- Dark mode background is lake-black: `#11161A`.
- Dark mode body text is pale blue-white: `#E8EDF2`.
- Fonts are self-hosted open-source fonts only:
  - Serif/prose: `Source Serif 4`, fallback `Georgia, serif`.
  - Sans/meta: `IBM Plex Sans`, fallback `Arial, sans-serif`.
  - Both families are stored under `static/fonts/` with their SIL OFL license files.
- Do not load fonts from Google Fonts, Adobe Fonts, or another runtime service.
- Do not use proprietary FT fonts such as Financier or Metric.
- Base font size is `16px` desktop and `15.5px` mobile.
- Primary page measure is `700px`.
- Homepage/About prose and banner measure is narrower than the page: `440px`, so home/About text and banner right edges share the same bound and keep matching line rhythm.
- On mobile, home/About prose and banners stop about `40px` before the right page edge; note prose and small banners keep the narrower `48px` right-side breathing room.
- Main page width is `min(calc(100% - 128px), 700px)`.
- Mobile page width is `min(calc(100% - 32px), 700px)`.
- Links are visually plain until hover. Do not add blue link styling except if a future design explicitly asks for it.
- Public navigation is intentionally minimal: homepage, About link from intro copy, and click-in posts. There is no top nav and no section-only browsing page.
- Theme defaults to the visitor's `prefers-color-scheme`, then persists manual light/dark selection in `localStorage`.
- Browser tab title is always lowercase `public thoughts`.
- Favicon uses lowercase `db` on a bright on-theme blue background so it stays visible in crowded tab stacks.
- Share previews use Open Graph and Twitter Card metadata with absolute URLs. Post pages use the post title, single-line description/summary, publish time, and required cover image. About uses the About banner; home uses the homepage banner.
- Prefer a concise `description` in frontmatter when the automatic summary would start with a list, formatting artifact, or placeholder text.
- Post cover images can be static `/images/...` files or bundle-local files such as `banner.jpg`; both resolve for page display and share metadata.

## Homepage Template

- Top padding: `64px` desktop, `36px` mobile.
- Homepage title contains only: `BY DEXTER BOSLEY`.
- No byline, email, nav, logo, button, or top hyperlink.
- Header stacks the site title and the quiet theme toggle.
- Header title:
  - font-family `IBM Plex Sans`
  - font-size `0.86rem`
  - font-weight `700`
  - uppercase
  - letter-spacing `0.04em`
  - color `#080808`
- Theme toggle labels are exactly `(*)` and `(o)`, visually hushed, and placed directly underneath `BY DEXTER BOSLEY`.
- Gap from header to intro: `80px` desktop, `72px` mobile.
- Intro copy uses `Source Serif 4` at the prose scale and is constrained to the narrower homepage prose measure.
- Homepage image is `/images/homepage-lake-annecy.jpeg`, placed between the second and third intro paragraphs.
- Homepage intro copy is two paragraphs around the banner:
  - before image: `Welcome to thinking in public. I never could journal so I'm trying this. After all, it doesn’t really count unless you write it down.`
  - after image: `You can read more about me here. Subscribe to free updates here. My thoughts below.`
- Keep `thinking in public` highlighted in the first paragraph.
- Keep the first `here` linked to `/about/`, the second `here` linked to `/subscribe/`, and both visibly underlined.
- Keep `My thoughts below` highlighted, with the period outside the highlight.
- Homepage image has no caption.
- Homepage image crop:
  - width matches the homepage/About prose measure, so its right edge aligns with the text column on desktop and mobile
  - height `265px` desktop
  - height `210px` mobile
  - `object-fit: cover`
  - `object-position: center 78%`
- Homepage sections are `START HERE` followed by `RECENT`.
- Start Here contains three placeholder best-of slots until real selections are chosen.
- Recent contains the curated public set plus static placeholders. The first real rows are `Placeholder`, `Useful Tools`, and `Small Talk`.
- Recent flips in place after 15 visible rows using component-level `Previous`/`Next` controls plus numbered page buttons. Use ellipses in the page controls when there are too many pages to show comfortably. Do not navigate to `/page/2/` for homepage or About Recent rows.
- Use blue highlights sparingly for one phrase per surface, not whole sentences.

## About Template

- About is a quick flip from the homepage, not a separate branded page.
- About header title is `ABOUT DEXTER BOSLEY`; the homepage header title remains `BY DEXTER BOSLEY`.
- Do not show an `About` page title.
- Render about text in the same narrow homepage prose measure.
- Include `/images/about-snow-banner.jpg` immediately after the first about paragraph, using the same banner dimensions as the homepage.
- Crop the About banner around the upper-middle of the photo so it balances sky with snow and trees.
- Render the remaining about copy below the banner in the same narrow text measure.
- End the About copy with highlighted `My thoughts below`, with the period outside the highlight.
- Do not include an `Elsewhere` heading or link cluster.
- Render the same `START HERE` and `RECENT` index tables below the banner.

## Index Rows

- The homepage index is curated, not automatically all posts.
- Do not generate or link to Essays-only or Stories-only index pages.
- Start Here row grid: read time, black horizontal rule, right-aligned title.
- Start Here placeholder read time is `1 MIN`.
- Recent row grid: date, black horizontal rule, right-aligned title.
- Dates appear in compact uppercase format: `MAR 30, 2026`.
- Homepage titles do not include post kind suffixes.
- Index row text uses `IBM Plex Sans`, uppercase, `0.07em` letter spacing.
- Homepage titles align right on desktop.
- Dates and read times are muted and lighter weight.
- On mobile, hide the horizontal rule and keep date/read time left with title right-aligned on the same row.

## Post Templates

- Essays, stories, and notes have explicit templates:
  - `layouts/essays/single.html`
  - `layouts/stories/single.html`
  - `layouts/notes/single.html`
  - shared renderer: `layouts/partials/post-single.html`
- Post pages do not show the homepage header.
- Post canvas width matches the homepage: `min(calc(100% - 96px), 700px)` desktop and `min(calc(100% - 32px), 700px)` mobile.
- Post padding matches the homepage: `64px 0 88px` desktop and `36px 0 64px` mobile.
- Post header contains title, the quiet `(*)` / `(o)` theme toggle, then the date, Back, and Share utilities.
- On desktop widths of `1100px` and up, those utilities move into a quiet left rail beside the reading column.
- Below `1100px`, the utilities stay as a compact left-aligned stack under the title/toggle.
- The utility stack uses caption-like treatment: muted, sans, about `0.76rem`, light letter spacing, and compact actions formatted as `<- BACK` and `^ SHARE`.
- Post date format is compact uppercase: `MAR 30, 2026`.
- Read estimate is not shown in click-in post headers.
- Post title:
  - font-family `Source Serif 4`
  - font-size `1.28rem`
  - font-weight `600`
  - line-height `1.18`
  - no forced uppercase
- Post date:
  - muted `#777`
  - font-family `IBM Plex Sans`
  - font-size about `0.76rem`
- Gap from post header to body: roughly `2.5rem`.
- Post body:
  - font-family `Source Serif 4`
  - font-size `1.04rem`
  - line-height about `1.66`
  - paragraph margin-bottom about `1.65rem`
- Post footer actions:
  - Use a black, in-theme action row.
  - Left action is `<- BACK` and always points to `/`.
  - Right action is `^ SHARE` and should use native share when available, otherwise copy/prompt the current post URL.
  - Do not use red for post actions.
- Top post actions are caption-scaled, more restrained than the footer, and should not reuse the heavy bordered footer treatment.
- Native share uses the post title rather than the browser tab title.

## Essay Structure

- Essays require `cover.image`, `cover.alt`, and `cover.caption` in frontmatter.
- The cover renders between the compact header actions and `## **I.** ***Title***`.
- Essay summaries are not required and should not be used as a default post primitive.
- Essays use Roman numeral section headings with bold numerals and bold italic section titles as the only divider system.
- Section headings should be `## **I.** ***First***`, `## **II.** ***Next***`, `## **III.** ***Last***`, and so on.
- Do not use `---`, `***`, horizontal rules, ornaments, or centered asterisks in essays.
- The stylesheet hides accidental essay `<hr>` output, but authors should still write Roman section headings.

## Story Structure

- Stories require `cover.image`, `cover.alt`, and `cover.caption` in frontmatter.
- The cover renders between the compact header actions and `## **I.** ***Title***`.
- Stories start directly after the banner pause with `## **I.** ***First***`.
- Story and essay banner images share the same treatment:
  - width `100%`
  - height `250px` desktop
  - height `190px` mobile
  - `object-fit: cover`
  - `object-position: center`
- Essays and stories use a larger gap after the banner so the first section does not crowd the image.
- Stories use Roman numeral section headings with bold numerals and bold italic section titles, matching essays.
- Section headings should be `## **I.** ***First***`, `## **II.** ***Next***`, and so on.
- Do not use `***` story dividers.

## Notes Structure

- Notes are the third public post type.
- Notes live in `content/notes/`.
- Notes follow a short, tweet-like format: title, quiet theme toggle, compact utility row, small banner, then body.
- Notes require `cover.image`, `cover.alt`, and `cover.caption` in frontmatter.
- Note body text uses the same narrow measure as the homepage and About copy.
- Note banners use the homepage/About banner treatment:
  - max-width `420px`
  - height `210px` desktop
  - height `175px` mobile
  - `object-fit: cover`
- Notes should not require Roman numeral essay sections or story scene breaks.
- Use notes for short public journal entries, working observations, and quick updates.

## Highlights

- Highlight primitive is native HTML: `<mark>highlighted phrase</mark>`.
- Highlight colors:
  - Light mode best: `#1F4E67`
  - Light mode popular/recent: `#2F6F8F`
  - Light mode inline: `#DBE6F1`
  - Dark mode best: `#6FA9C7`
  - Dark mode popular/recent: `#4F88A8`
  - Dark mode inline: `#2A3E4C`
- Inline highlights use `.highlight-inline`.
- Section highlights use `.section-highlight` plus the relevant palette class.
- Section highlights use white text in both light and dark mode.
- Padding is `0.02em 0.2em 0.06em`.
- Highlights should feel like a soft annotation, not a callout. Use on short phrases only.
- Hugo allows raw HTML via `[markup.goldmark.renderer] unsafe = true` for this primitive.

## Images And Captions

- Placeholder images may live under `static/images/placeholders/` while layout is being reviewed; replace them with real images before final publication when possible.
- Essays, stories, and notes use a banner image with caption.
- Hugo build validation fails click-in posts that are missing `cover.image`, `cover.alt`, or `cover.caption`.
- Preferred post storage is a Hugo leaf bundle: `content/<section>/<post-slug>/index.md` plus local image files.
- Bundle image names:
  - `banner.jpg` or `banner.png` for the required top/share image
  - `figure-01.png`, `figure-02.jpg` for graphs, screenshots, and inline figures
  - `book-cover-01.jpg` and `album-cover-01.jpg` for cover references
- Essays should add images only when they are intentional figures, diagrams, or graphs.
- Image markdown pattern:
  - `![Alt text](/images/file.jpg)`
  - blank line
  - `*Caption text.*`
- Banner and figure caption formats:
  - Location/photo/painting: `City/Place, Country - photo` or `City/Place, Country - painting`
  - Artwork/book/album cover: `Name (year), Artist`
  - Graph/screenshot/report: `Source: Source name (year). Note: short context.`
- In post pages, Markdown image paragraphs are centered.
- Essay and story images, graphs, and screenshots should not run full width by default; they use `max-width: 580px` inside the `700px` column. Do not add per-kind shortcodes or raw HTML figure systems unless explicitly requested.
- Image margin starts at `3rem` above image and `0.75rem` below.
- Captions use `IBM Plex Sans`, not italic visually:
  - `font-style: normal`
  - font-size about `0.76rem`
  - line-height about `1.45`
- Keep captions short and descriptive.

## Future Post Starter Shapes

- Essay archetype includes:
  - frontmatter with required cover fields
  - Roman numeral headings with bold numerals and bold italic section titles
  - body text with optional `<mark>`
  - image and caption pattern
  - bundle starter at `archetypes/essay-bundle/index.md`
- Story archetype includes:
  - frontmatter with required cover fields
  - Roman numeral headings with bold numerals and bold italic section titles
  - prose sections
  - bundle starter at `archetypes/story-bundle/index.md`
- Note archetype includes:
  - frontmatter with required small banner cover fields
  - short body text
  - bundle starter at `archetypes/note-bundle/index.md`

## What Not To Add

- No cards.
- No rounded UI.
- No hero image.
- No decorative gradients.
- No nav unless explicitly requested.
- No email/byline under the homepage title unless explicitly requested.
- No external fonts.
- No complex JavaScript for reading behavior: no progress bar, sticky mini reader header, toast, or scroll chrome.
- No standard quote component; quotes are not part of the default essay/story/note system.

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
  - `dexterbosley.com/templates/essay-bundle/index.md`
  - `dexterbosley.com/templates/story-bundle/index.md`
  - `dexterbosley.com/templates/note-bundle/index.md`
- Publish from Terminal:
  - `cd /Users/dexterbosley/projects/dexterbosley.com`
  - `./publish.sh "Update journal"`
- Publishing rebuilds `docs/`, commits all site changes, and pushes to GitHub Pages.
