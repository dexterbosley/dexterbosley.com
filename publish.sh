#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
exec python3 scripts/editor.py --publish --message "${1:-Update dexterbosley.com}"
