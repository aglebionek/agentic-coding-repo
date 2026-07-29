#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${AGENTIC_REPO_URL:-https://github.com/aglebionek/agentic-coding-repo}"
BRANCH="${AGENTIC_BRANCH:-main}"
DEST_DIR="${AGENTIC_TARGET_DIR:-$(pwd)}"

require_cmd() {
    command -v "$1" >/dev/null 2>&1 || {
        echo "Missing required command: $1" >&2
        exit 1
    }
}

require_cmd mktemp
require_cmd cp
require_cmd mv
require_cmd rm
require_cmd cmp
require_cmd diff

TMP_DIR="$(mktemp -d)"
trap 'rm -rf -- "$TMP_DIR"' EXIT

resolve_source_root() {
    if [[ -n "${AGENTIC_SOURCE_DIR:-}" ]]; then
        printf '%s\n' "$AGENTIC_SOURCE_DIR"
        return
    fi

    require_cmd curl
    require_cmd tar
    require_cmd find

    local archive_url="$REPO_URL/archive/refs/heads/$BRANCH.tar.gz"
    local archive_path="$TMP_DIR/repo.tar.gz"
    local extract_dir="$TMP_DIR/extracted"
    local extracted_root

    echo "Downloading shared agent assets from $archive_url" >&2
    curl -fsSL "$archive_url" -o "$archive_path"
    mkdir -p "$extract_dir"
    tar -xzf "$archive_path" -C "$extract_dir"

    extracted_root="$(find "$extract_dir" -mindepth 1 -maxdepth 1 -type d -print -quit)"
    if [[ -z "$extracted_root" ]]; then
        echo "Failed to locate extracted repository contents." >&2
        exit 1
    fi

    printf '%s\n' "$extracted_root"
}

require_source_asset() {
    local source_path="$1"

    if [[ ! -e "$source_path" ]]; then
        echo "Missing required shared source asset: $source_path" >&2
        exit 1
    fi
}

SOURCE_ROOT="$(resolve_source_root)"
SOURCE_ROOT="$(cd "$SOURCE_ROOT" && pwd)"
DEST_DIR="$(cd "$DEST_DIR" && pwd)"

SHARED_SOURCE="$SOURCE_ROOT/shared"
SKILLS_SOURCE="$SOURCE_ROOT/skills"

required_files=(
    "AGENTS_TEMPLATE.md"
    "BASE_AGENT_GUIDELINES.md"
    "ARCHITECTURE_GUIDELINES.md"
    "CODING_GUIDELINES.md"
    "TESTING_GUIDELINES.md"
    "AGENTIC_GLOSSARY.md"
)

for file_name in "${required_files[@]}"; do
    require_source_asset "$SHARED_SOURCE/$file_name"
done
require_source_asset "$SKILLS_SOURCE"

STAGED_MANAGED_DIR="$TMP_DIR/managed"
mkdir -p "$STAGED_MANAGED_DIR"

for file_name in "${required_files[@]}"; do
    cp "$SHARED_SOURCE/$file_name" "$STAGED_MANAGED_DIR/$file_name"
done
cp -R "$SKILLS_SOURCE" "$STAGED_MANAGED_DIR/skills"

MANAGED_DIR="$DEST_DIR/.agentic"
rm -rf -- "$MANAGED_DIR"
mv "$STAGED_MANAGED_DIR" "$MANAGED_DIR"

for file_name in "${required_files[@]}"; do
    echo "Installed .agentic/$file_name"
done
echo "Installed .agentic/skills/"

if [[ ! -e "$DEST_DIR/AGENTS.md" ]]; then
    echo "No project-owned AGENTS.md found. Create one from the managed template:"
    echo "  cp .agentic/AGENTS_TEMPLATE.md AGENTS.md"
else
    echo "Project-owned AGENTS.md preserved. Managed template: .agentic/AGENTS_TEMPLATE.md"
fi

if [[ -f "$DEST_DIR/CODING_GUIDELINES.md" ]] &&
   cmp -s "$DEST_DIR/CODING_GUIDELINES.md" "$SHARED_SOURCE/CODING_GUIDELINES.md"; then
    echo "Legacy root CODING_GUIDELINES.md matches the shared asset; review it manually."
fi

if [[ -d "$DEST_DIR/skills" ]] &&
   diff -qr "$DEST_DIR/skills" "$SKILLS_SOURCE" >/dev/null 2>&1; then
    echo "Legacy root skills/ matches the shared assets; review it manually."
fi

echo "Shared agent assets installed in: $MANAGED_DIR"
echo "Fill project-specific placeholders only in the root AGENTS.md copy."
