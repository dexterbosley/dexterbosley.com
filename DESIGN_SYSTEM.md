# DexterBosley.com Design System

A public journal for essays, stories, notes, and small observations. The site should feel like a careful index and reading surface: plain, literary, quiet, slightly terminal-adjacent, and self-contained.

## Surface

- The site is light-only: `--bg #fdfdfb`, `--ink #151412`, `--muted #6b6964`, `--wash #e4e9f1`, `--frame #151412`.
- Link tokens: `#0000EE`, visited `#551A8B`, active `#FF0000`, hover `#0000C4`.
- Blue means an unread writing link; purple means already read; muted grey means interface furniture.
- Nothing on the page should be blue unless clicking it gives the reader something to read.
- No cards, rounded corners, shadows, decorative rules, gradient decoration, section fills, or dot separators.
- Use spacing, line breaks, and parentheses for hierarchy.

## Typography

- Serif: self-hosted Newsreader variable `opsz,wght`, then `Georgia`, `"Times New Roman"`, serif.
- Sans/interface: self-hosted IBM Plex Sans, then Arial, Helvetica, sans-serif.
- Type tokens live in `assets/css/site.css`. They use rem units with a 16px browser default: body 17px, index titles 18px, page titles 20px, metadata and captions 12px, interface labels 13px, tables 14px, and form inputs 16px.
- Keep the root at 100% so browser text preferences work. Form inputs stay at 16px to avoid focus zoom on mobile.
- Type size does not scale with viewport width.
- Home and archive row titles are uppercase serif bold at `--type-entry`. Page and post titles use `--type-title`. Browser tab titles are uppercase across the site.
- Interface text is IBM Plex Sans, using `--type-ui` and `--type-small`.
- The masthead uses IBM Plex Sans at `--type-entry` (18px), matching the home row title size.
- Prose letter spacing is zero. Uppercase sans labels use modest positive tracking.

## Home

- Place a hushed row of `about`, `email`, and `linkedin` directly under `BY DEXTER BOSLEY`.
- Home image is object-width, left-aligned, 11:7 crop, no visible caption, meaningful alt text.
- Object width is `min(60%, 384px)` and relaxes to `min(72%, 384px)` at `480px` and below.
- Subscribe is unboxed: one email input and the filled `receive` button. It is the only filled element on the page.
- The subscribe form is up to 384px wide and can use the full mobile column so the email field remains usable.
- `POPULAR` uses the curated starter pages; `POSTS` uses `home_recent: true` sorted newest first.
- Section labels are bold ink uppercase with no updated-date line.
- Rows show title, type, date, and read time with spacing and no separators. Notes are labeled `comment`.
- Footer is hushed and includes `about`, `email`, `linkedin`, and `© 2026`, in that order.
- About uses a short professional bio and Goya's public-domain *The Dog*, with the same object width and 11:7 crop as the home photo. Position the crop to keep the dog visible. Its footer replaces `about` with `< back`.

## Posts And Content

- Essays, stories, and notes render through `layouts/partials/post-single.html`.
- Post headers include title, date, and `< BACK` stacked above `^ SHARE`. The bottom navigation includes `<- BACK` and `^ SHARE`.
- Essay and story covers use the same full-column width and 11:7 aspect ratio, aligned with the text's left edge.
- `^ SHARE` uses the native share sheet where available and copies the URL otherwise.
- All posts require `description`, `cover.image`, `cover.alt`, and `cover.caption`.
- Essays and stories use Roman section headings such as `## **I.**`.
- Notes may start directly.
- Notes do not render a visible cover banner, but cover fields still drive metadata and link cards.
- Body images, graphs, figures, and tables share a centered `min(100%, 580px)` content-object width inside the `640px` reading column.
- Charts and tables scroll within their own container on narrow screens. Keep chart labels at their desktop reading size instead of shrinking them to fit a phone.
- Tables use a plain reading treatment like Codex tables: 14px sans-serif type, semibold headers, light horizontal row separators, no outer or vertical borders, no header fill, and comfortable cell padding. Keep equal `2.25rem` spacing before and after and horizontal scrolling on narrow screens. Comparison colors belong in row labels rather than filled rows.
- Use native `<mark>` only for short inline prose highlights; `--wash` is for highlights and selection, not labels or section backgrounds.

## Distribution Infrastructure

- Canonical feed URL is `/index.xml`; do not add `/rss.xml`.
- RSS is full-content and must use absolute URLs inside `content:encoded`.
- Pages emit canonical URLs, RSS alternate link, Open Graph, Twitter card metadata, `theme-color`, favicon, and apple touch icon.
- Share images are 1200x630. Use post cover art when available and the default ink-on-paper `BY DEXTER BOSLEY` card otherwise.
- Keep `robots.txt`, `sitemap.xml`, `/404.html`, and `/archive/` working.
- GoatCounter is the only analytics script. Track subscribe attempts and outbound email/LinkedIn clicks. Subscription results belong to the newsletter service.
- CSS and JavaScript are minified, fingerprinted build assets shared by every page. Preload the regular reading and interface fonts only. Italics load when needed.
- All raster images used by templates belong in `assets/images` or a page bundle. Hugo generates WebP and fallback sizes automatically, with intrinsic dimensions. Match each `sizes` attribute to the CSS width. Above-fold images load eagerly, body images load lazily.

## Newsletter

- Homepage subscribe must work without JavaScript via listmonk's plain form endpoint.
- Use listmonk's native form result until a readable cross-origin API response is available. Never infer success from an opaque `no-cors` response. The optional name on the subscribe page must submit without JavaScript.
- Email export writes local HTML by default.
- Draft listmonk campaign creation is opt-in via environment variables and must remain idempotent by slug/title.
- Never commit listmonk credentials or sender secrets.

## Do Not Add

- Marketing hero layouts, product-page framing, cards, badges, filled labels, decorative horizontal rules, sticky reader chrome, progress bars, toasts, or frameworks.
- Third-party font requests.
- Homepage decks.
- A second feed URL.
