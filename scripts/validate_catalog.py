#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from catalog_lib import SKILL_ROOT, load_catalog


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    errors = []
    catalog = load_catalog()
    asset_index = json.loads((SKILL_ROOT / "data/assets_index.json").read_text(encoding="utf-8"))
    products = catalog.get("products", [])
    ids = [p.get("id") for p in products]
    if len(products) != catalog.get("record_count"):
        errors.append("record_count does not match products length")
    if len(ids) != len(set(ids)):
        errors.append("duplicate product IDs")
    required = {"id", "product_type", "name_zh_tw", "key_ingredients_text", "functions_text", "official_url", "image", "data_gaps"}
    valid_ids = set(ids)
    for p in products:
        missing = sorted(required - set(p))
        if missing:
            errors.append(f"{p.get('id')}: missing fields {missing}")
        path = (SKILL_ROOT / p.get("image", "")).resolve()
        if not path.is_file():
            errors.append(f"{p.get('id')}: missing image {path}")
        if SKILL_ROOT.resolve() not in path.parents:
            errors.append(f"{p.get('id')}: image escapes skill root")
        for component in p.get("components", []):
            if component not in valid_ids:
                errors.append(f"{p.get('id')}: unknown component {component}")
    indexed = {a["product_id"]: a for a in asset_index.get("product_assets", [])}
    for p in products:
        record = indexed.get(p["id"])
        if not record:
            errors.append(f"{p['id']}: missing asset index entry")
            continue
        path = SKILL_ROOT / record["path"]
        if path.is_file() and sha256(path) != record["sha256"]:
            errors.append(f"{p['id']}: asset hash mismatch")
    for style in asset_index.get("style_references", []):
        path = SKILL_ROOT / style["path"]
        if not path.is_file():
            errors.append(f"missing style reference {path}")
        elif sha256(path) != style["sha256"]:
            errors.append(f"style hash mismatch {path.name}")
    result = {
        "ok": not errors,
        "products": len(products),
        "product_assets": len(asset_index.get("product_assets", [])),
        "style_references": len(asset_index.get("style_references", [])),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
