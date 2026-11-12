# Writing on dexterbosley.com

## On this computer

Double-click **Dexter Writing Desk** on the desktop. It opens a small local editor in your browser. The essay **On B2C Shopping Agents** opens first.

1. Choose a page on the left and edit its Markdown.
2. Click **Save & preview** (or Ctrl+S / Cmd+S). This writes the file locally and rebuilds the real site preview. Switch the preview to **Phone** to check tables and images.
3. Review **Saved changes**, then click **Publish saved changes**. This builds the production site, checks links, images, feeds, forms, and table formatting, commits the saved site files, and pushes to GitHub. GitHub Pages normally updates the live site in about a minute. The editor reports the push, not deployment completion; check the live site afterward.

Saving never publishes. Unsaved edits are not included in publication. All saved changes under `content/`, `assets/`, `static/`, and generated `docs/` are included, not just the selected page. Other changed project files block publication so they can be handled separately in Git. A failed push can be retried with Publish.

## Files you own

The editor is just a view of ordinary UTF-8 Markdown files. You can also use VS Code, Obsidian, Notepad, or another editor on the same files:

| What | File or folder |
| --- | --- |
| Shopping agents essay | `content/essays/on-unserious-thinking.md` |
| Other essays | `content/essays/` |
| Stories | `content/stories/` |
| Notes | `content/notes/` |
| About page | `content/about.md` |
| Shared source images | `assets/images/` or `static/images/` |
| Last saved copies | `.local-editor/backups/` |

The shopping essay's filename is historical. Its `slug: on-shopping-agents` keeps the public URL stable. **Do not edit `docs/`**: Hugo rebuilds that folder. There is no separate copy of your essay to keep synchronized.

Keep Markdown table rows adjacent, with no blank lines between the header, separator, and rows. Blank lines turn tables into ordinary text. Publication checks catch this.

The editor keeps a local backup before each save. If another editor changes a file while it is open, saving stops rather than overwriting it. Copy the unsaved text, then reload and compare. Backups stay on this machine and are not sent to GitHub.

## New writing

Use **New essay, story, or note**. New pages start with `draft: true` and a placeholder cover. Open **Page settings** to edit the title, description, date, cover image, alt text, and caption. Set `draft: false` when ready to appear on the live site. Drafts appear in the local preview but not in the production build. A future date also keeps a page off the live site until it is rebuilt after that date.

For images, put a file beside a new bundle's `index.md` and reference its filename in Markdown or `cover.image`. Existing image conventions and newsletter notes are in `OBSIDIAN_WORKFLOW.md`.

## On another desktop

Install **Python 3.10 or newer** and **Git**, and authenticate Git with your GitHub account (for example through Git Credential Manager). Clone the repository into a local folder:

```sh
git clone https://github.com/dexterbosley/dexterbosley.com.git
cd dexterbosley.com
```

Then:

- **Windows:** double-click `Write.cmd`.
- **macOS:** run `chmod +x Write.command` once, then double-click it, or run `python3 scripts/editor.py` in Terminal.
- **Linux:** run `python3 scripts/editor.py`.

On first launch, the editor downloads Hugo **0.157.0** from its official GitHub release and verifies the release checksum. No Python packages, Node, account for the editor, or cloud editor service are needed. Setup requires internet; editing and previewing afterward work offline. GitHub authentication is required only for sync and publish. The editor listens only on this computer's loopback address.

Before editing on a second computer, click **Get latest from GitHub**. Publish from the first computer first. Never use two computers to edit an unsynchronized copy simultaneously. Sync requires a clean working copy; publishing refuses to overwrite newer remote commits. If both computers changed files, reconcile them in Git before publishing. Prefer separate clones over syncing the `.git` folder through OneDrive.

Commits use your Git identity if configured. Otherwise they are labeled `Local editor <local-editor@localhost>`. To set your preferred identity for this clone:

```sh
git config user.name "Dexter Bosley"
git config user.email "YOUR_GITHUB_EMAIL"
```

The terminal launcher stays running while the editor is open. Ctrl+C stops it; closing the browser tab alone does not stop the server. The desktop shortcut on this machine runs it without a terminal; its process details and logs are under `.local-editor/`. Reopening the shortcut reuses the running editor. To stop that background process, run the local `.local-editor/stop.ps1` script in PowerShell.

## Verify the workflow

```sh
python scripts/test_editor.py
python scripts/check_site.py
```

The editor tests use temporary repositories and a local bare remote; they never publish to the real website.
