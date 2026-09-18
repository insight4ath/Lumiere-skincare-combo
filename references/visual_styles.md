# Social image styles and production rules

## Default: `luxury-warm-minimal`

Use the images in `assets/style-references/` only as style, layout and typography references.

- Warm white to pale beige seamless studio.
- Ivory cylindrical and square architectural pedestals at varied heights.
- Soft diffused daylight from the upper left with restrained long shadows.
- Low-saturation ivory, cream, pale beige and light gray palette.
- Photorealistic commercial beauty photography; realistic frosted glass, matte plastic and metal.
- Warm charcoal body text and muted taupe-gold combination name.
- No flowers, leaves, water splashes, droplets, fabric, people, prices, badges or added slogans.

## Optional creative variants

- `clinical-clean`: white and pale gray, crisp softbox light, strict grid, minimal shadow.
- `fresh-aqua`: cool white and very pale blue, translucent acrylic pedestals; no water or droplets unless the user explicitly requests them.
- `night-luxe`: charcoal-to-warm-black studio, controlled gold rim light, enough contrast to preserve white packaging.
- `soft-pastel`: warm blush or sand background, restrained tonal pedestals, no decorative props by default.

These variants are creative directions, not source-backed product facts. Package colors and labels remain unchanged.

## Layout by product count

- **1–2 products:** generous negative space; product group may occupy 45–60% of the canvas.
- **3 products:** staggered lower-half pedestals; keep one clear editorial text zone.
- **4 products:** use lower 50–60% for products and a two-column copy grid above when copy is required.
- **5+ products:** prioritize packaging visibility. Consider a separate copy slide if text would become too small.

## Ratio handling

- Default: `1:1` square.
- Instagram portrait: `4:5`; keep important labels and copy inside central safe margins.
- Story/Reel: `9:16`; increase vertical spacing and avoid placing copy at interface edges.
- Never stretch or distort products to fit a ratio. Recompose the scene.

## Text hierarchy

1. Combination name: small editorial overline, muted taupe-gold.
2. Product name: larger dark warm gray.
3. `關鍵成分｜…`: smaller body text.
4. `主要功能｜…`: smaller body text.

Use exact Traditional Chinese. No extra headline or English translation unless requested. When copy is dense, generate the product photograph first and add typography in a second edit. Re-check every character.

## Product identity invariants

- Use exactly one instance of each selected product unless duplicates are explicitly requested.
- Preserve bottle/jar proportions, cap, dropper, pump, spoon or applicator, logo, label layout, wording and color.
- A detached dropper in a source image does not authorize an extra loose dropper in the final composition. Prefer the container closed unless the user asks otherwise.
- Applicators belonging to jars may be included once and must not be counted as another product.
- Do not use a completed style reference as a product source.

## Prompt skeleton

```text
Use case: ads-marketing
Asset type: <ratio> social skincare campaign
Primary request: Create a product-faithful campaign image for exactly <count> selected products.
Input images: Image 1 is style-only; remaining images are hard product-identity references.
Scene/style: <style profile>
Composition: <count-aware layout and text zone>
Text (verbatim): <combination name and product copy>
Critical invariants: preserve package geometry, cap/pump, logo, label, wording, color and material.
Avoid: substitutions, duplicates, extra products, wrong text, price, discount, badge, extra copy and unrequested props.
```

