# DexterBosley.com Design System

A public journal for essays, stories, notes, and small observations. The site should feel like a careful index and reading surface: plain, literary, quiet, slightly terminal-adjacent, and self-contained.

## Surface

- Light tokens: `--bg #fdfdfb`, `--ink #151412`, `--muted #76746f`, `--wash #e4e9f1`, `--accent #23456e`, `--frame #151412`.
- Dark tokens: `--bg #0c0c0e`, `--ink #e6e4de`, `--muted #9a9993`, `--wash #1c2536`, `--accent #7d9cce`, `--frame #e6e4de`.
- Link tokens: light `#0000EE`, visited `#551A8B`, active `#FF0000`, hover `#0000C4`; dark link `#7d9cce`, visited `#a493c4`, active `#d08a8a`, hover `#9db8e0`.
- The light muted token is slightly darker than the original mockup so the 9px `UPDATED` line clears contrast.
- Blue means an unread writing link; purple means already read; muted grey means interface furniture.
- Nothing on the page should be blue unless clicking it gives the reader something to read.
- No cards, rounded corners, shadows, decorative rules, gradient decoration, section fills, or dot separators.
- Use spacing, line breaks, and parentheses for hierarchy.

## Typography

- Serif: self-hosted Newsreader variable `opsz,wght`, then `Georgia`, `"Times New Roman"`, serif.
- Sans/interface: self-hosted IBM Plex Sans, then Arial, Helvetica, sans-serif.
- Body size is controlled by `--body`: standard `17px`, small `15px`, large `21px`.
- Type size does not scale with viewport width.
- Post row titles are serif bold at `calc(var(--body) + 1px)`.
- Decks are serif italic muted at `calc(var(--body) - 2px)`.
- Interface text is IBM Plex Sans: masthead `13px`, labels `13px`, updated line `9px`, metadata/footer/contact `11px`.
- Prose letter spacing is zero. Uppercase sans labels use modest positive tracking.

## Home

- Header order: `BY DEXTER BOSLEY`, display controls `(*) (o) (-)`, then `email` and `linkedin` stacked.
- Header contact links are hushed: muted, uppercase, no underline until hover, and no visited color.
- `rss` never appears in the header.
- Text-size button glyphs: standard `(-)`, large `(^)`, small `(v)`.
- The text-size strip reads `TEXT SIZE: SMALL STANDARD LARGE`; selected option is bold ink.
- Home image is object-width, left-aligned, 11:7 crop, no visible caption, meaningful alt text.
- Object width is `min(60%, 384px)` and relaxes to `min(72%, 384px)` at `480px` and below.
- Subscribe is unboxed: one email input and the filled `receive` button. It is the only filled element on the page.
- `POPULAR` uses the curated starter pages; `POSTS` uses `home_recent: true` sorted newest first.
- Section labels are bold ink uppercase, followed by `UPDATED <MONTH YYYY>` from the newest date in that section.
- Row deck policy is `deck`, then `description`, then no deck. Never generate a truncated summary deck.
- Footer is hushed and includes `email`, `linkedin`, `rss`, `archive`, and `© 2026`; `rss` links to `/index.xml`.

## Posts And Content

- Essays, stories, and notes render through `layouts/partials/post-single.html`.
- Post pages include title, display controls, date, `<- BACK`, and `^ SHARE`.
- `^ SHARE` uses the native share sheet where available and copies the URL otherwise.
- All posts require `description`, `cover.image`, `cover.alt`, and `cover.caption`.
- `deck` is optional and only affects homepage rows.
- Essays and stories use Roman section headings such as `## **I.** ***First***`.
- Notes may start directly.
- Notes do not render a visible cover banner, but cover fields still drive metadata and link cards.
- Use native `<mark>` only for short inline prose highlights; `--wash` is for highlights and selection, not labels or section backgrounds.

## Distribution Infrastructure

- Canonical feed URL is `/index.xml`; do not add `/rss.xml`.
- RSS is full-content and must use absolute URLs inside `content:encoded`.
- Pages emit canonical URLs, RSS alternate link, Open Graph, Twitter card metadata, `theme-color`, favicon, and apple touch icon.
- Share images are 1200x630. Use post cover art when available and the default ink-on-paper `BY DEXTER BOSLEY` card otherwise.
- Keep `robots.txt`, `sitemap.xml`, `/404.html`, and `/archive/` working.
- GoatCounter is the only analytics script. Track subscribe attempts/results and outbound email/linkedin/rss/archive clicks.

## Newsletter

- Homepage subscribe must work without JavaScript via listmonk's plain form endpoint.
- JavaScript may intercept the form for inline success/error messaging and should avoid listmonk's default confirmation page when available.
- Email export writes local HTML by default.
- Draft listmonk campaign creation is opt-in via environment variables and must remain idempotent by slug/title.
- Never commit listmonk credentials or sender secrets.

## Do Not Add

- Marketing hero layouts, product-page framing, cards, badges, filled labels, decorative horizontal rules, sticky reader chrome, progress bars, toasts, or frameworks.
- Third-party font requests.
- Machine-generated homepage decks.
- A second feed URL.
