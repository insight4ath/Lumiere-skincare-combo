# Lumiere-skincare-combo

這是一個可分享、可安裝的 Codex Skill。它內建若美芙產品資料、產品圖片與視覺參考，可依自然語言需求完成產品查詢、保養組合建議，以及社群商品圖片提示詞與生成流程。

## 主要功能

- 依乾燥、保濕、熟齡、提亮、毛孔、舒緩等需求選品
- 指定必選或排除產品，控制組合件數
- 檢查 A 醇、酸類與防曬等搭配限制
- 取得產品關鍵成分、功能與本機圖片路徑
- 生成 1:1、4:5 等社群商品圖所需的結構化提示詞
- 使用產品原圖作為硬性識別參考，避免改變包裝與品牌文字

## 安裝

將整個 `lumiere-skincare-combo` 資料夾放入 Codex 的 skills 目錄，或使用本專案的 ZIP 安裝包。

## 使用範例

```text
使用 $lumiere-skincare-combo 幫我搭配乾燥熟齡肌四件組，並生成高級奶油極簡風的 IG 4:5 商品圖。
```

```text
使用 $lumiere-skincare-combo 搭配三件提亮保養，必須包含紅妍保濕水凝霜，並列出關鍵成分與功能。
```

## 資料說明

- `data/products.json`：32 項產品的結構化資料
- `assets/products/`：32 張產品圖片
- `assets/style-references/`：5 張精品暖白極簡風格參考圖
- `references/`：搭配規則、資料結構與視覺規範
- `scripts/`：產品查詢、組合推薦、提示詞建立與資料驗證工具

即時售價、完整 INCI 與未經來源驗證的膚質分類不在資料庫中；Skill 會標記缺漏，不會自行臆造。

## 驗證

```bash
python scripts/validate_catalog.py
python scripts/product_lookup.py --need hydration --need anti-aging --limit 8
python scripts/recommend_bundle.py --needs hydration,anti-aging --count 4 --include-name 紅妍保濕水凝霜 --json
```
