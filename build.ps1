# Build script for normalizacja-liczebnikow
# Regenerates the dist/ directory with a fresh build

$ErrorActionPreference = "Stop"

# Remove existing dist/
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist"
}

# Build the package
uv run python -m build --outdir dist/

# Print shared instructions
Get-Content "$PSScriptRoot\post-build-message.txt"
