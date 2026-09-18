#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

from catalog_lib import match_name, products, with_absolute_path

CONFLICT_A = {"retinoid"}
CONFLICT_B = {"exfoliating-acid", "physical-exfoliant"}


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def conflict(left: dict, right: dict) -> bool:
    a = set(left["active_flags"])
    b = set(right["active_flags"])
    return bool((a & CONFLICT_A and b & CONFLICT_B) or (b & CONFLICT_A and a & CONFLICT_B))


def role_penalty(candidate: dict, selected: list[dict]) -> int:
    roles = set(candidate["routine_roles"])
    selected_roles = [set(item["routine_roles"]) for item in selected]
    penalty = 0
    if "moisturizer" in roles and any("moisturizer" in item for item in selected_roles):
        penalty += 18
    if ("exfoliant" in roles or "mild-exfoliant" in roles) and any("exfoliant" in item or "mild-exfoliant" in item for item in selected_roles):
        penalty += 30
    if "sunscreen" in roles and any("sunscreen" in item for item in selected_roles):
        penalty += 50
    return penalty


def candidate_score(product: dict, needs: set[str], selected: list[dict], count: int) -> int:
    score = 25 * len(needs & set(product["derived_need_tags"]))
    roles = set(product["routine_roles"])
    score += 5 if "serum" in roles else 0
    score += 8 if "moisturizer" in roles and not any("moisturizer" in p["routine_roles"] for p in selected) else 0
    active_request = bool(needs & {"brightening", "exfoliation", "anti-aging", "fine-lines"})
    if active_request and count >= 3 and "sunscreen" in roles:
        score += 22
    return score - role_penalty(product, selected)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a deterministic starting bundle from the 若美芙 catalog.")
    parser.add_argument("--needs", required=True, help="Comma-separated derived need tags")
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--include-id", action="append", default=[])
    parser.add_argument("--include-name", action="append", default=[])
    parser.add_argument("--exclude-id", action="append", default=[])
    parser.add_argument("--include-sets-tools", action="store_true")
    parser.add_argument("--allow-conflicting-actives", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.count < 1:
        raise SystemExit("--count must be at least 1")
    needs = set(parse_csv(args.needs))
    all_products = products()
    allowed = [p for p in all_products if args.include_sets_tools or p["product_type"] == "formula"]
    excluded = set(args.exclude_id)
    allowed = [p for p in allowed if p["id"] not in excluded]

    selected = []
    warnings = []
    required_tokens = list(args.include_id) + list(args.include_name)
    for token in required_tokens:
        matched = next((p for p in allowed if p["id"] == token or match_name(p, token)), None)
        if not matched:
            raise SystemExit(f"Required product not found or excluded: {token}")
        if matched not in selected:
            selected.append(matched)
    if len(selected) > args.count:
        raise SystemExit("Required products exceed requested count")

    active_request = bool(needs & {"brightening", "exfoliation", "anti-aging", "fine-lines"})
    if active_request and args.count >= 3 and not any("sunscreen" in p["routine_roles"] for p in selected):
        sunscreen = next((p for p in allowed if "sunscreen" in p["routine_roles"] and p not in selected), None)
        if sunscreen and len(selected) < args.count:
            selected.append(sunscreen)

    while len(selected) < args.count:
        candidates = []
        for product in allowed:
            if product in selected:
                continue
            if not args.allow_conflicting_actives and any(conflict(product, item) for item in selected):
                continue
            score = candidate_score(product, needs, selected, args.count)
            candidates.append((score, -product["catalog_number"], product))
        if not candidates:
            warnings.append("No additional compatible product was available for the requested count.")
            break
        candidates.sort(reverse=True, key=lambda item: (item[0], item[1]))
        selected.append(candidates[0][2])

    if any("retinoid" in p["active_flags"] for p in selected):
        warnings.append("Introduce retinoid gradually at night; use daily sunscreen; seek medical guidance during pregnancy or breastfeeding.")
    if any(set(p["active_flags"]) & CONFLICT_B for p in selected):
        warnings.append("Introduce exfoliation gradually and use daily sunscreen.")
    if args.allow_conflicting_actives and any(conflict(a, b) for i, a in enumerate(selected) for b in selected[i + 1:]):
        warnings.append("Retinoid and exfoliant are both present: schedule them on separate nights, never in the same routine.")
    if any(p["price_twd"] is None for p in selected):
        warnings.append("Current prices are not embedded; do not calculate a bundle total without official live verification.")

    result = {
        "requested_needs": sorted(needs),
        "requested_count": args.count,
        "selected_count": len(selected),
        "products": [with_absolute_path(p) for p in selected],
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for p in result["products"]:
            print(f"{p['id']}\t{p['name_zh_tw']}\t{p['image_absolute']}")
        for warning in warnings:
            print(f"WARNING\t{warning}")


if __name__ == "__main__":
    main()
