#!/bin/bash

# Stop on any error
set -e

echo "🧹 Cleaning up old files..."
# Remove the output folder and the stray index file in root if it exists
rm -rf docs
rm -f index.html

echo "🏗️  Building site..."
# Hugo will build to 'docs/' based on your config
hugo

echo "🔍 Verifying links..."
# Check for localhost links in the new build
if grep -q "localhost:1313" docs/index.html; then
    echo "❌ ERROR: Found 'localhost' links! Check your baseURL in hugo.toml."
    exit 1
fi

echo "✅ Links look good (dexterbosley.com detected)."

echo "📦 Committing to Git..."
git add .

echo "📝 Enter commit message:"
read msg
git commit -m "$msg"

echo "🚀 Pushing to GitHub..."
git push origin main

echo "🎉 Deployed successfully!"
