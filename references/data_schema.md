# Catalog schema and provenance

## Files

- `data/products.json`: primary runtime catalog.
- `data/assets_index.json`: image path, dimensions, SHA-256 and original filename.
- `data/source_catalog.xlsx`: audited source workbook retained for provenance; runtime scripts do not require Excel.
- `assets/products/LDV-TW-###.jpg`: normalized product images.
- `assets/style-references/*.png`: completed campaign examples used only as style/layout references.

## Product fields

| Field | Meaning |
|---|---|
| `id` | Stable skill identifier. |
| `product_type` | `formula`, `set`, or `tool`. |
| `name_zh_tw` | Audited Traditional Chinese product name. |
| `key_ingredients_text` | Source-backed ingredient/material summary. |
| `key_ingredients` | Mechanically split helper list; use the text field when wording matters. |
| `functions_text` | Source-backed cosmetic function summary. |
| `official_url` | Taiwan official product page. |
| `audit_note` | Regional differences, non-disclosure, or set/tool qualifications. |
| `image` | Skill-relative asset path. |
| `routine_roles` | Derived selection helper. |
| `derived_need_tags` | Derived keyword tags for matching requests. |
| `active_flags` | Derived active-family markers used for compatibility checks. |
| `usage_constraints` | General skincare safeguards derived from active flags. |
| `components` | Product IDs contained in a prebuilt set. |
| `price_twd` | `null` until a complete current official price is verified. |
| `data_gaps` | Fields the catalog does not establish. |

## Data boundaries

- `key_ingredients_text` is not a complete INCI list.
- `derived_need_tags` are routing aids, not diagnoses or official suitability claims.
- Do not infer undisclosed surfactants, exact tool metals, clinical efficacy, or current pricing.
- Regional formula differences are resolved in favor of the Taiwan listing and noted in `audit_note`.

