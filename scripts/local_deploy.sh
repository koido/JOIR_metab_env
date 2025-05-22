#!/usr/bin/env bash
# Build MkDocs site and serve locally for preview

set -euo pipefail

PORT=${1:-8000}

# Build site into ./site directory
mkdocs build --clean

# Serve the built site
echo "Serving documentation on http://localhost:${PORT}"
python3 -m http.server "${PORT}" --directory site

