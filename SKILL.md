---
name: lumiere-skincare-combo
description: Select and combine bundled Lumière de Vie／若美芙 skincare products by skin concern, routine role, required items, and social-image brief, then generate product-faithful social campaign images from the included local assets. Use for 若美芙 product lookup, routine or bundle recommendations, ingredient/function copy, and social product-image generation; do not use for unrelated brands or medical diagnosis.
---

# Lumiere-skincare-combo

Use the bundled catalog and product images. Do not ask the user to upload or download assets already present in this skill.

## Source of truth

- Read `data/products.json` for product names, key ingredients, functions, official links, audit notes, derived tags, and image paths.
- Read `data/assets_index.json` when verifying asset integrity or locating style references.
- Treat `key_ingredients_text`, `functions_text`, `official_url`, and `audit_note` as source-backed fields.
- Treat `routine_roles`, `derived_need_tags`, `active_flags`, and `usage_constraints` as helper fields derived for selection. Do not present them as manufacturer wording.
- Prices are intentionally `null` because the source catalog does not contain complete current prices. If the user requests a priced bundle, verify current official Taiwan prices when live browsing is available; otherwise disclose that exact pricing cannot be calculated. Never invent prices.

## Route the request

1. Extract the requested skin concerns, product count, required or excluded products, routine timing, budget, audience, image ratio, visual style, and whether copy must appear in the image.
2. For product search, run `scripts/product_lookup.py`.
3. For a proposed bundle, read `references/combination_rules.md`, then run `scripts/recommend_bundle.py` as a starting point. Review its output before presenting it.
4. For an image request, also read `references/visual_styles.md`. Run `scripts/render_prompt.py` to produce exact product paths and a structured prompt.
5. Inspect every selected local product image before generation. Use the absolute paths returned by the scripts as image references.
6. Generate with the available image-generation tool. Treat every product image as a hard identity reference: preserve package geometry, cap or pump, brand mark, label, wording, color, and material.
7. Inspect the result for product count, duplication, package fidelity, exact copy, and requested aspect ratio. Make one targeted correction when needed.
8. Save final project-bound images outside the installed skill or in the user's requested destination. Do not overwrite source assets.

## Bundle requirements

- Honor required products and exact item count.
- Prefer complementary routine roles and avoid accidental duplicate formulas or a prebuilt set plus its component products.
- Do not place a retinoid and strong exfoliant in the same routine. They may appear in one advanced multi-night plan only when the schedule clearly separates them.
- Pair exfoliating or retinoid routines with daytime sunscreen guidance.
- Use cosmetic wording such as “改善外觀” or “有助於”; do not diagnose or promise medical treatment.
- Flag sensitive-skin introduction, patch testing, and retinoid pregnancy or breastfeeding caution when relevant.

## Image requirements

- Default to a 1:1 social image only when the user does not specify a ratio.
- Use exactly the selected products. No duplicates, substitutions, invented variants, or added props that imply another product.
- Keep ingredient and function copy verbatim from `products.json`, shortening only when the user asks or layout requires it; if shortened, preserve the meaning and never invent an ingredient.
- For dense copy or three-plus products, prefer a two-pass workflow: first compose the product photograph, then add exact typography while preserving the image.
- Never add price, discount, badges, extra claims, or promotional copy unless explicitly requested and sourced.

## Useful commands

```bash
python scripts/product_lookup.py --need hydration --need anti-aging --limit 8
python scripts/recommend_bundle.py --needs hydration,anti-aging --count 4 --include-name 紅妍保濕水凝霜 --json
python scripts/render_prompt.py --ids LDV-TW-018,LDV-TW-008 --title 基礎補水組 --style luxury-warm-minimal --ratio 1:1
python scripts/validate_catalog.py
```

## Example requests

- `幫我搭配乾燥熟齡肌4件組，做成高級奶油極簡風IG 4:5商品圖。`
- `一定要有紅妍保濕水凝霜，搭3組不同預算的提亮保養；沒有即時價格就先列產品、不臆算。`
- `找出含A醇或酸類的產品，說明不能同晚搭配的項目。`
