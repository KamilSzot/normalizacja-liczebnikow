#!/usr/bin/env bash
# Build script for normalizacja-liczebnikow
# Regenerates the dist/ directory with a fresh build

set -euo pipefail

# Remove existing dist/
rm -rf dist/

# Build the package
uv run python -m build --outdir dist/

# Print shared instructions
cat "$(dirname "$0")/post-build-message.txt"
