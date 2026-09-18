#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

from catalog_lib import normalize, products, with_absolute_path


def score_product(product: dict, queries: list[str], needs: list[str], roles: list[str]) -> int:
    searchable = normalize(" ".join([
        product["id"], product["name_zh_tw"], product["key_ingredients_text"],
        product["functions_text"], " ".join(product["derived_need_tags"]),
        " ".join(product["routine_roles"]), " ".join(product["active_flags"]),
    ]))
    score = 0
    for query in queries:
        q = normalize(query)
        if q == normalize(product["id"]) or q == normalize(product["name_zh_tw"]):
            score += 100
        elif q in searchable:
            score += 20
    score += 15 * len(set(needs) & set(product["derived_need_tags"]))
    score += 12 * len(set(roles) & set(product["routine_roles"]))
    return score


def main() -> None:
    parser = argparse.ArgumentParser(description="Search the bundled 若美芙 catalog.")
    parser.add_argument("--query", action="append", default=[], help="Text query; repeatable")
    parser.add_argument("--need", action="append", default=[], help="Derived need tag; repeatable")
    parser.add_argument("--role", action="append", default=[], help="Routine role; repeatable")
    parser.add_argument("--type", choices=["formula", "set", "tool"])
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    found = []
    for product in products():
        if args.type and product["product_type"] != args.type:
            continue
        score = score_product(product, args.query, args.need, args.role)
        if (args.query or args.need or args.role) and score == 0:
            continue
        found.append((score, product["catalog_number"], product))
    found.sort(key=lambda item: (-item[0], item[1]))
    output = [with_absolute_path(item[2]) for item in found[: max(args.limit, 0)]]

    if args.json:
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return
    for product in output:
        print(f"{product['id']}\t{product['name_zh_tw']}\t{','.join(product['routine_roles'])}\t{','.join(product['derived_need_tags'])}\t{product['image_absolute']}")


if __name__ == "__main__":
    main()

