#!/usr/bin/env bash
set -euo pipefail

message="${1:-Update dexterbosley.com}"

hugo --cleanDestinationDir

git add -A

if git diff --cached --quiet; then
    echo "No site changes to publish."
    exit 0
fi

git commit -m "$message"
git push origin main
