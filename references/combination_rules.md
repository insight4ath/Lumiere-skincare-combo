# Product combination rules

Use these rules when selecting products or reviewing `recommend_bundle.py` output.

## Need mapping

| User wording | Preferred need tags or roles |
|---|---|
| 乾燥、缺水、脫屑 | `hydration`, `dryness`; hydration serum plus moisturizer |
| 出油、毛孔、粗糙 | `oil-control`, `pores`, `exfoliation`; niacinamide or controlled exfoliation |
| 暗沉、膚色不均、斑點 | `brightening`, `antioxidant`; vitamin C or spot treatment plus sunscreen |
| 敏弱、屏障不穩 | `soothing`, `barrier-support`; avoid stacking strong actives |
| 初老、細紋 | `fine-lines`, `firmness`, `anti-aging`; peptide or hydration treatment |
| 熟齡、明顯皺紋 | anti-aging treatment plus moisturizer and sunscreen; introduce retinoid gradually |
| 眼周暗沉或疲態 | `eye-area`; eye cream or eye mask |
| 身體乾燥 | `body-care`; do not substitute facial products without explanation |

## Composition by requested count

- **2 items:** one targeted treatment plus one moisturizer, or moisturizer plus sunscreen for a daytime brief.
- **3 items:** one or two compatible treatments plus moisturizer; use sunscreen as the third item for daytime brightening, exfoliating, or retinoid-focused requests.
- **4 items:** build a complete sequence such as cleanser/toner, treatment, moisturizer, sunscreen. For advanced nighttime routines, a second treatment is acceptable when their schedules do not conflict.
- **5+ items:** separate morning and evening roles. Avoid filling the count with redundant moisturizers, multiple exfoliants, or cosmetic tools unless requested.

## Compatibility and scheduling

- Do not use retinoid and exfoliating acid or physical exfoliation in the same routine.
- Do not select more than one exfoliant unless the user explicitly asks for alternatives rather than simultaneous use.
- If a bundle contains both retinoid and exfoliant, label it as a multi-night plan and assign different nights.
- Introduce retinoid, mandelic/lactic acid, AHA products, and exfoliating masks gradually.
- Recommend daily sunscreen with retinoids, exfoliants, vitamin C brightening, or pigment-focused routines.
- Vitamin C and niacinamide can be placed in one broader routine, but sensitive users should introduce products one at a time.
- A prebuilt set counts as one sellable item but already contains its component formulas. Do not add the same component separately unless the user requests duplication.

## Required and excluded items

- Required products override scoring but not safety. Keep them and adjust the remaining roles.
- Exclusions are absolute unless they make the request impossible; then explain the conflict.
- Match normalized product names and IDs, but show the audited Traditional Chinese name to users.

## Budget handling

The embedded catalog has no complete current pricing. When a budget is specified:

1. If official Taiwan price lookup is available, verify each selected product and record the as-of date.
2. If live lookup is unavailable, do not calculate a total. Offer a product-count or simple/standard/premium structure and state that exact prices require verification.
3. Do not reuse stale prices from examples as current prices.

## Consumer-safety wording

- Present skincare recommendations as general cosmetic guidance, not medical care.
- Suggest patch testing and gradual introduction for active products.
- Advise people who are pregnant, trying to conceive, or breastfeeding to seek medical guidance before retinoid use.
- Persistent irritation, severe acne, eczema, or rosacea should be evaluated by a qualified clinician.

