#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/aglebionek/agentic-coding-repo"
BRANCH="main"

require_cmd() {
command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    exit 1
}
}

require_cmd curl
require_cmd tar
require_cmd mktemp
require_cmd cp
require_cmd find

DEST_DIR="$(pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

ARCHIVE_URL="$REPO_URL/archive/refs/heads/$BRANCH.tar.gz"
ARCHIVE_PATH="$TMP_DIR/repo.tar.gz"
EXTRACT_DIR="$TMP_DIR/extracted"

echo "Downloading from $ARCHIVE_URL"
curl -fsSL "$ARCHIVE_URL" -o "$ARCHIVE_PATH"

mkdir -p "$EXTRACT_DIR"
tar -xzf "$ARCHIVE_PATH" -C "$EXTRACT_DIR"

ROOT_DIR="$(find "$EXTRACT_DIR" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
if [[ -z "$ROOT_DIR" ]]; then
echo "Failed to locate extracted repo contents." >&2
exit 1
fi

copy_if_exists() {
local src="$1"
local dest="$2"

if [[ -e "$src" ]]; then
    rm -rf "$dest"
    cp -R "$src" "$dest"
    echo "Copied $(basename "$dest")"
else
    echo "Skipping missing path: $src" >&2
fi
}

copy_if_exists "$ROOT_DIR/AGENTS.md" "$DEST_DIR/AGENTS.md"
copy_if_exists "$ROOT_DIR/GLOSSARY.md" "$DEST_DIR/GLOSSARY.md"
copy_if_exists "$ROOT_DIR/skills" "$DEST_DIR/skills"

echo "Done. Files copied into: $DEST_DIR"