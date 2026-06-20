# DexterBosley.com Design System

A plain public journal: quiet, editorial, document-like. Do not make it feel like a product page, portfolio, magazine, or theme demo.

## Surface

- Light: background `#fff`, text `#080808`.
- Dark: background `#11161A`, text `#E8EDF2`.
- Serif/prose: self-hosted `Source Serif 4`, then `Georgia, serif`.
- Sans/meta: self-hosted `IBM Plex Sans`, then `Arial, sans-serif`.
- No Google Fonts, Adobe Fonts, or proprietary FT fonts.
- Measure: `700px`; homepage/About prose and banners: about `440px`.
- Main width: `min(calc(100% - 128px), 700px)` desktop, `min(calc(100% - 32px), 700px)` mobile.
- Browser title stays `public thoughts`.
- Theme follows system preference until the visitor chooses light/dark.

## Home And About

- Header text: Home `BY DEXTER BOSLEY`; About `ABOUT DEXTER BOSLEY`.
- Theme toggle labels stay `(*)` and `(o)`.
- No top nav, byline, logo, or button.
- Home intro uses the lake banner; About uses the snow banner after the first paragraph.
- Banners align with the narrow text column and crop with `object-fit: cover`.
- Sections are `START HERE` then `RECENT`.
- Start Here links to `Small Talk`, `Useful Tools`, and `Tatie`.
- Recent pins `Tatie`, `Useful Tools`, and `Small Talk` first, then shows the remaining `home_recent: true` posts by date.
- Recent paginates in place after 10 rows, not with `/page/2/` navigation.

## Posts

- Essays, stories, and notes render through `layouts/partials/post-single.html`.
- Post pages hide the homepage header.
- Header includes title, theme toggle, date, `<- BACK`, and `^ SHARE`.
- At `1100px+`, utilities sit in the left rail; below that, they sit under the title.
- Essays and stories use Roman section headings: `## **I.** ***Title***`.
- Notes are short and do not need Roman sections.
- All posts require `cover.image`, `cover.alt`, and `cover.caption`.

## Images

- Templates use Hugo responsive image partials for WebP, fallback formats, dimensions, and load priority.
- Source images should live in page bundles or `assets/images/`; legacy `/static/images/` paths may remain for compatibility.
- New source image filenames use `post-title_full-caption-title_media-type.ext`, with lowercase kebab case in each segment.
- Valid media types are `image`, `graph`, `painting`, `photo`, and `review`.
- Use `review` for book, album, and movie collateral; review images share fixed `180px` by `270px` dimensions in post bodies.
- Bundle convention: `index.md`, a descriptive cover image, optional descriptive figure or review images.
- Markdown figure pattern: image line, blank line, italic caption line.
- Markdown review-image pattern: image line with title `"review"`, blank line, italic caption line.
- Caption examples: `City, Country`; `Name (year), Artist`; `Source: Name (year). Note: context.`
- Captions use the formal title/place/source structure only; do not append media-type suffixes such as `- photo` or `- painting`.

## Highlights

- Use native `<mark>` for short phrases only.
- Inline highlights use `.highlight-inline`; section labels use `.section-highlight`.
- Keep highlights sparse: one phrase per surface is usually enough.

## Do Not Add

- Cards, hero layouts, decorative gradients, rounded UI, or extra nav.
- External fonts.
- Reading progress bars, sticky reader chrome, toasts, or quote components.
- Scheduled publishing, monitors, notifications, or background agents.
