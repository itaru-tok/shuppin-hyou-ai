# shuppin-hyou-ai

中古車の出品表から、
- テキストの抽出（位置情報付き bbox）
- 車体展開図の bbox
を返すプロトタイプ。

## 目的（PoC）
- Azure OCR で文字 + bbox を取得
- YOLO で車体図の bbox を検出
- LLM で最終の項目抽出/補正（誤字・表記ゆれ）
- JSON を統合出力

## ディレクトリ構成
- `data/raw/`  元画像
- `data/ocr/`  OCR結果
- `data/yolo/` YOLO用ラベル
- `outputs/`   推論結果JSON
- `scripts/`   実行スクリプト
- `src/`       共通ロジック

## セットアップ（venv）
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

必要に応じて追加:
```bash
pip install -r requirements-azure.txt
pip install -r requirements-llm.txt
```

## 実行の流れ（予定）
1. 画像収集 → `data/raw/`
2. OCR実行 → `data/ocr/`
3. YOLO学習 → `data/yolo/`
4. 推論 → `outputs/`

## 評価指標（予定）
- OCR: 文字一致率（CER）
- K/V: キーと値の一致率（F1）
- 図bbox: IoU（予測枠と正解枠の重なり率）
- 速度: 1画像あたりの平均処理時間
- コスト: 1画像あたりのAPI費用

## LLMの役割（予定）
- OCR誤字の補正（表記ゆれの正規化）
- 項目抽出（車名/年式/走行距離など）
- 曖昧な候補がある場合の優先順位付け

## TODO
- [ ] Azure OCR スクリプト作成
- [ ] YOLO 学習・推論スクリプト作成
- [ ] LLM 補正スクリプト作成
- [ ] 統合JSON生成
- [ ] 評価スクリプト作成
