#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = SKILL_ROOT / "data/products.json"


def load_catalog() -> dict:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def products() -> list[dict]:
    return load_catalog()["products"]


def absolute_image(product: dict) -> str:
    return str((SKILL_ROOT / product["image"]).resolve())


def normalize(value: str) -> str:
    return "".join(value.lower().split()).replace("（", "(").replace("）", ")")


def match_name(product: dict, query: str) -> bool:
    q = normalize(query)
    name = normalize(product["name_zh_tw"])
    return q in name or name in q or q == normalize(product["id"])


def with_absolute_path(product: dict) -> dict:
    result = dict(product)
    result["image_absolute"] = absolute_image(product)
    return result

