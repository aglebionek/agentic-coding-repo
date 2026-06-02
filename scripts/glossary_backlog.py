#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_BACKLOG_PATH = Path(
    os.environ.get("GLOSSARY_BACKLOG_PATH", "/tmp/agentic-coding-glossary-backlog.json")
)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def normalize_term(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")


def build_item_id(kind: str, term: str, conflict_with: str | None) -> str:
    base = f"{kind}-{normalize_term(term) or 'item'}"
    if conflict_with:
        return f"{base}-vs-{normalize_term(conflict_with) or 'term'}"
    return base


def load_backlog(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "items": []}

    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict) or "items" not in data or not isinstance(data["items"], list):
        raise ValueError(f"Invalid backlog file: {path}")

    return data


def write_backlog(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", delete=False, dir=path.parent, encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=True)
        handle.write("\n")
        tmp_path = Path(handle.name)

    tmp_path.replace(path)


def pending_items(data: dict[str, Any]) -> list[dict[str, Any]]:
    return [item for item in data["items"] if item.get("status") != "resolved"]


def unique_append(values: list[Any], candidate: Any) -> None:
    if candidate and candidate not in values:
        values.append(candidate)


def format_evidence(item: dict[str, Any]) -> str:
    parts = []
    for evidence in item.get("evidence", []):
        source = evidence.get("source")
        context = evidence.get("context")
        if source and context:
            parts.append(f"{source}: {context}")
        elif context:
            parts.append(context)
        elif source:
            parts.append(source)
    return "; ".join(parts)


@dataclass
class CaptureArgs:
    path: Path
    term: str
    reason: str
    kind: str
    source: str | None
    context: str | None
    conflict_with: str | None


def capture_item(args: CaptureArgs) -> int:
    data = load_backlog(args.path)
    item_id = build_item_id(args.kind, args.term, args.conflict_with)
    normalized_term = normalize_term(args.term)
    normalized_conflict = normalize_term(args.conflict_with or "")

    existing = next(
        (
            item
            for item in data["items"]
            if item.get("id") == item_id
            or (
                item.get("kind") == args.kind
                and item.get("normalized_term") == normalized_term
                and item.get("normalized_conflict_with", "") == normalized_conflict
            )
        ),
        None,
    )

    if existing is None:
        existing = {
            "id": item_id,
            "term": args.term,
            "normalized_term": normalized_term,
            "kind": args.kind,
            "status": "pending",
            "occurrences": 0,
            "reasons": [],
            "evidence": [],
            "created_at": now_iso(),
            "updated_at": now_iso(),
        }
        if args.conflict_with:
            existing["conflict_with"] = args.conflict_with
            existing["normalized_conflict_with"] = normalized_conflict
        data["items"].append(existing)

    existing["status"] = "pending"
    existing["term"] = args.term
    existing["updated_at"] = now_iso()
    existing["occurrences"] = int(existing.get("occurrences", 0)) + 1
    unique_append(existing.setdefault("reasons", []), args.reason)

    evidence: dict[str, str] = {}
    if args.source:
        evidence["source"] = args.source
    if args.context:
        evidence["context"] = args.context
    if evidence:
        unique_append(existing.setdefault("evidence", []), evidence)

    write_backlog(args.path, data)
    print(f"Captured {existing['id']} in {args.path}")
    return 0


def list_items(path: Path, as_json: bool) -> int:
    data = load_backlog(path)
    items = pending_items(data)
    if as_json:
        print(json.dumps(items, indent=2, ensure_ascii=True))
        return 0

    if not items:
        print(f"No pending glossary backlog items in {path}")
        return 0

    print(f"Pending glossary backlog items in {path}:")
    for item in items:
        conflict = f" vs {item['conflict_with']}" if item.get("conflict_with") else ""
        reasons = "; ".join(item.get("reasons", []))
        evidence = format_evidence(item)
        print(f"- {item['id']}: {item['term']}{conflict} [{item['kind']}]")
        if reasons:
            print(f"  reason: {reasons}")
        if evidence:
            print(f"  evidence: {evidence}")
    return 0


def handoff(path: Path, glossary: str) -> int:
    data = load_backlog(path)
    items = pending_items(data)
    if not items:
        print(f"No pending glossary backlog items in {path}")
        return 0

    print("# Glossary backlog handoff")
    print()
    print("## Inputs")
    print(f"- Glossary: `{glossary}`")
    print(f"- Backlog: `{path}`")
    print()
    print("## Pending items")
    print()
    for index, item in enumerate(items, start=1):
        heading = f"{index}. **{item['term']}**"
        if item.get("conflict_with"):
            heading += f" vs **{item['conflict_with']}**"
        heading += f" (`{item['kind']}`)"
        print(heading)
        for reason in item.get("reasons", []):
            print(f"   - Why: {reason}")
        for evidence in item.get("evidence", []):
            source = evidence.get("source")
            context = evidence.get("context")
            if source and context:
                print(f"   - Evidence: {source}: {context}")
            elif context:
                print(f"   - Evidence: {context}")
            elif source:
                print(f"   - Evidence: {source}")
    print()
    print("## Prompt")
    print("```")
    print(
        f"Read {glossary} and {path}. Review all pending glossary backlog items, update only the glossary, "
        "keep entries concise, and reconcile resolved backlog items when the glossary clearly covers them."
    )
    print("```")
    return 0


def resolve_items(path: Path, ids: list[str], terms: list[str], note: str | None, reopen: bool) -> int:
    if not ids and not terms:
        raise ValueError("At least one --id or --term is required")

    data = load_backlog(path)
    term_keys = {normalize_term(term) for term in terms}
    status = "pending" if reopen else "resolved"
    changed: list[str] = []

    for item in data["items"]:
        if item.get("id") in ids or item.get("normalized_term") in term_keys:
            item["status"] = status
            item["updated_at"] = now_iso()
            if note:
                item["resolution_note"] = note
            elif not reopen and "resolution_note" not in item:
                item["resolution_note"] = "Resolved from glossary review"
            changed.append(item["id"])

    if not changed:
        print("No matching glossary backlog items found", file=sys.stderr)
        return 1

    write_backlog(path, data)
    action = "Reopened" if reopen else "Resolved"
    print(f"{action}: {', '.join(changed)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage a deferred glossary backlog.")
    parser.add_argument("--path", type=Path, default=DEFAULT_BACKLOG_PATH, help="Backlog JSON path")
    subparsers = parser.add_subparsers(dest="command", required=True)

    capture = subparsers.add_parser("capture", help="Capture or merge a glossary candidate")
    capture.add_argument("--term", required=True, help="Primary term or concept")
    capture.add_argument("--reason", required=True, help="Why the item belongs in the glossary backlog")
    capture.add_argument(
        "--kind",
        choices=["repeated", "conflict", "missing", "requested"],
        required=True,
        help="Why this candidate was captured",
    )
    capture.add_argument("--source", help="File, discussion, or other source")
    capture.add_argument("--context", help="Short evidence or surrounding context")
    capture.add_argument("--conflict-with", help="Competing term for conflict items")

    show = subparsers.add_parser("list", help="List pending glossary backlog items")
    show.add_argument("--json", action="store_true", help="Emit JSON instead of text")

    handoff_parser = subparsers.add_parser("handoff", help="Print an aggregated glossary handoff")
    handoff_parser.add_argument("--glossary", default="./GLOSSARY.md", help="Glossary path to reference")

    resolve = subparsers.add_parser("resolve", help="Mark items resolved")
    resolve.add_argument("--id", action="append", default=[], help="Backlog item id")
    resolve.add_argument("--term", action="append", default=[], help="Resolve by normalized term")
    resolve.add_argument("--note", help="Resolution note")

    reopen = subparsers.add_parser("reopen", help="Reopen resolved items")
    reopen.add_argument("--id", action="append", default=[], help="Backlog item id")
    reopen.add_argument("--term", action="append", default=[], help="Reopen by normalized term")
    reopen.add_argument("--note", help="Reason for reopening")

    subparsers.add_parser("path", help="Print the active backlog path")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "capture":
            return capture_item(
                CaptureArgs(
                    path=args.path,
                    term=args.term,
                    reason=args.reason,
                    kind=args.kind,
                    source=args.source,
                    context=args.context,
                    conflict_with=args.conflict_with,
                )
            )
        if args.command == "list":
            return list_items(args.path, args.json)
        if args.command == "handoff":
            return handoff(args.path, args.glossary)
        if args.command == "resolve":
            return resolve_items(args.path, args.id, args.term, args.note, reopen=False)
        if args.command == "reopen":
            return resolve_items(args.path, args.id, args.term, args.note, reopen=True)
        if args.command == "path":
            print(args.path)
            return 0
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 1

    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
