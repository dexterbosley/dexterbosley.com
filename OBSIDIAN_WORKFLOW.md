# DexterBosley.com Workflow

For the desktop editor, Save & Preview, Publish, and setup on another computer, start with [WRITING.md](WRITING.md). The source of truth is the existing `content/` directory.

Run commands from the root of the `dexterbosley.com` repository. Edit source files, then rebuild `docs/` before publishing. Use Hugo 0.157.0 to keep generated output consistent.

## Preview And Build

```sh
hugo server -D
hugo --cleanDestinationDir
python3 scripts/check_site.py
```

Only publish when Dexter explicitly asks. Publishing rebuilds `docs/`, commits, and pushes:

```sh
./publish.sh "Update journal"
```

## Design Source Of Truth

`DESIGN_SYSTEM.md` is the current source of truth. It supersedes older Reverso prototypes and previous rules about Source Serif, filled section labels, boxed subscribe forms, old Start Here/Recent behavior, and hidden top contact links.

## Required Frontmatter

```yaml
---
title: "Post Title"
date: 2026-06-08
draft: false
type: essay
description: "One clean sentence for link previews."
deck: ""
cover:
  image: "post-title_city-country-photo_photo.jpg"
  alt: "Short description"
  caption: "City, Country"
home_recent: true
---
```

- Use `type: essay`, `type: story`, or `type: note`.
- `description` is required for link previews. Home rows show title and metadata without a deck.
- Essays and stories usually start with Roman headings like `## **I.** ***First***`; notes can start directly.
- Notes still require cover fields for metadata/share images, but do not render a visible cover banner.

## Images

Use a bundle when a post has local images:

```text
content/essays/post-slug/
  index.md
  post-slug_caption-title_photo.jpg
  post-slug_caption-title_graph.png
  post-slug_caption-title_review.jpg
```

Use source image filenames in the format `post-title_full-caption-title_media-type.ext`, with lowercase kebab case in each segment. Valid media types are `image`, `graph`, `painting`, `photo`, and `review`.

Markdown figure pattern:

```md
![Alt text](post-title_source-name-2026-note-short-context_graph.png)

*Source: Source name (year). Note: short descriptive caption.*
```

Markdown review-image pattern:

```md
![Review item alt text](post-title_name-year-artist_review.jpg "review")

*Name (year), Artist.*
```

## Newsletter And Analytics

- Subscribe form endpoint: `https://newsletter.dexterbosley.com/subscription/form`
- Fetch endpoint for enhanced subscribe: `https://newsletter.dexterbosley.com/api/public/subscription`
- listmonk list UUID: `853dabc3-3d14-4070-92d6-95f37ad85ae9`
- Sender: `Dexter Bosley <updates@dexterbosley.com>`
- Analytics dashboard: `https://dexterbosley.goatcounter.com`
- GoatCounter is the only analytics script.

Keep secrets out of the repo. Resend API keys, listmonk credentials, and PikaPods credentials stay in their dashboards or a private password manager.

The site uses the native form endpoint. Do not restore an inline success message with `no-cors` fetch. An opaque response cannot confirm a subscription. Test the form structure and validation without subscribing real addresses.

## Pre-Publish Checklist

1. Run `hugo --cleanDestinationDir`.
2. Run `python3 scripts/check_site.py` for local links, asset integrity, feeds, forms, and loading budgets.
3. Review home, essay, story, note, archive, about, subscribe, and 404 at desktop and mobile widths. Check for horizontal page overflow and unreadable text.
4. Confirm the home header shows `BY DEXTER BOSLEY` without navigation links, followed by the photo, subscribe form, `PINNED`, and `POSTS`. Footer contains About, email, LinkedIn, and copyright. Back and Share appear only in the top header of interior pages.
5. Confirm titles and browser tabs are uppercase. Post navigation has `< BACK` above `^ SHARE`.
6. Confirm the photo is responsive, has intrinsic dimensions, and uses a generated WebP instead of the full source JPEG. Confirm CSS and JavaScript are shared fingerprinted assets.
7. Confirm forms have a real no-JS `action` and `method`, and invalid email input is rejected before submission.
8. Confirm `/index.xml` contains full post bodies, absolute image/link URLs, and `atom:link rel="self"`.
9. Confirm canonical URLs, RSS alternate links, OG/Twitter metadata, favicon, apple touch icon, and theme-color metadata. Check `/robots.txt`, `/sitemap.xml`, `/404.html`, and `/archive/`.
10. Confirm GoatCounter appears only in production output. After pushing, verify the live HTML and assets.

## Email Export And Campaign Drafts

Export a post after building:

```sh
python3 scripts/export_email.py notes/tatie
```

Optionally create an idempotent draft listmonk campaign:

```sh
LISTMONK_URL="https://newsletter.dexterbosley.com" \
LISTMONK_USERNAME="..." \
LISTMONK_PASSWORD="..." \
LISTMONK_LIST_ID="..." \
python3 scripts/export_email.py notes/tatie --create-campaign
```

`LISTMONK_API_TOKEN` may be used instead of username/password if the server supports it. `LISTMONK_TEMPLATE_ID` is optional. If required env vars are missing, the script still exports local HTML and prints the missing setup.

The script refuses campaign creation when the rendered email lacks `{{ UnsubscribeURL }}`.

## External Follow-Ups

- Submit `https://www.dexterbosley.com/sitemap.xml` in Google Search Console.
- Verify SPF, DKIM, and DMARC pass for Resend/domain mail.
- Style the listmonk confirm-opt-in email in listmonk admin: plain, serif, no branding.
- Validate `https://www.dexterbosley.com/index.xml` with the W3C feed validator after deploy.
- Cross-post short excerpts to LinkedIn with canonical links back to the site.
