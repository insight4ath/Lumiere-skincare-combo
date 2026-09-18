#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from catalog_lib import SKILL_ROOT, products, with_absolute_path


def parse_ids(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an image-generation brief from exact catalog records.")
    parser.add_argument("--ids", required=True, help="Comma-separated product IDs")
    parser.add_argument("--title", required=True)
    parser.add_argument("--style", default="luxury-warm-minimal")
    parser.add_argument("--ratio", default="1:1")
    parser.add_argument("--output", help="Optional JSON output path")
    args = parser.parse_args()

    index = {p["id"]: p for p in products()}
    selected = []
    for product_id in parse_ids(args.ids):
        if product_id not in index:
            raise SystemExit(f"Unknown product ID: {product_id}")
        selected.append(index[product_id])
    if not selected:
        raise SystemExit("No product IDs provided")

    style_candidates = sorted((SKILL_ROOT / "assets/style-references").glob(f"{args.style}-*.png"))
    style_path = str(style_candidates[0].resolve()) if style_candidates else None
    product_paths = [with_absolute_path(p)["image_absolute"] for p in selected]
    copy_blocks = []
    for p in selected:
        copy_blocks.append(f"{p['name_zh_tw']}\n關鍵成分｜{p['key_ingredients_text']}\n主要功能｜{p['functions_text']}")
    exact_copy = args.title + "\n\n" + "\n\n".join(copy_blocks)
    prompt = f"""Use case: ads-marketing
Asset type: {args.ratio} social skincare campaign
Primary request: Create a product-faithful {args.style} campaign image featuring exactly {len(selected)} selected products.
Input images: The first image, when supplied, is style-only. All product images are hard identity references.
Composition: Use a count-aware balanced arrangement with clear labels and a dedicated editorial text zone. Recompose for {args.ratio}; never stretch products.
Text (verbatim, Traditional Chinese):
「{exact_copy}」
Critical invariants: Preserve every package proportion, cap/dropper/pump, accessory, logo, label layout, original wording, color and material. Use exactly one of each selected product.
Avoid: substitutions, duplicates, extra products, invented ingredients or claims, price, discount, badge, extra copy, altered packaging and unrequested props.
"""
    result = {
        "title": args.title,
        "style": args.style,
        "ratio": args.ratio,
        "style_reference": style_path,
        "product_references": product_paths,
        "reference_paths": ([style_path] if style_path else []) + product_paths,
        "products": [{"id": p["id"], "name": p["name_zh_tw"]} for p in selected],
        "prompt": prompt,
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()

