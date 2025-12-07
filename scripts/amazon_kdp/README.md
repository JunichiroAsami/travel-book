# スクリプト集

このディレクトリには、章ごとのマークダウンファイルからAmazon KDP用Word文書を作成するためのスクリプトが含まれています。

## スクリプト一覧

### 1. create_combined_markdown.sh

章ごとのマークダウンファイルを結合して統合マークダウンファイルを作成します。

**入力**:
- quickstart.md
- preface.md
- chapter1_final.md 〜 chapter12_final.md
- afterword.md
- appendix_b_final.md
- appendix_c_final.md

**出力**:
- complete_manuscript_v18.md

**使用方法**:
```bash
cd /home/ubuntu/ai_travel_book_project/finals
chmod +x scripts/create_combined_markdown.sh
./scripts/create_combined_markdown.sh
```

### 2. convert_chapters_to_word.sh

各章のマークダウンファイルをPandocでWord形式に変換します。

**入力**:
- quickstart.md
- preface.md
- chapter1_final.md 〜 chapter12_final.md
- afterword.md
- appendix_b_final.md
- appendix_c_final.md
- complete_manuscript_v10.docx（参照用）

**出力**:
- chapter_00.docx 〜 chapter_16.docx

**使用方法**:
```bash
cd /home/ubuntu/ai_travel_book_project/finals
chmod +x scripts/convert_chapters_to_word.sh
./scripts/convert_chapters_to_word.sh
```

**必要なソフトウェア**:
- Pandoc (バージョン 2.0以降)

### 3. merge_word_files.py

17個のWordファイルを結合してAmazon KDP用の完成版を作成します。

**入力**:
- chapter_00.docx 〜 chapter_16.docx

**出力**:
- complete_manuscript_v18_final.docx

**使用方法**:
```bash
cd /home/ubuntu/ai_travel_book_project/finals
python3.11 scripts/merge_word_files.py
```

**必要なライブラリ**:
```bash
pip3 install python-docx
```

### 4. verify_word_structure.py

Word文書の見出し構造を確認します。

**入力**:
- Word文書ファイル（デフォルト: complete_manuscript_v18_final.docx）

**出力**:
- 見出し構造の確認結果（標準出力）

**使用方法**:
```bash
cd /home/ubuntu/ai_travel_book_project/finals
python3.11 scripts/verify_word_structure.py [ファイル名]
```

**例**:
```bash
python3.11 scripts/verify_word_structure.py complete_manuscript_v18_final.docx
```

**必要なライブラリ**:
```bash
pip3 install python-docx
```

## 完全なワークフロー

以下の手順で、章ごとのマークダウンファイルからAmazon KDP用Word文書を作成できます：

### ステップ1: 統合マークダウンファイルを作成（オプション）

```bash
cd /home/ubuntu/ai_travel_book_project/finals
chmod +x scripts/create_combined_markdown.sh
./scripts/create_combined_markdown.sh
```

### ステップ2: 各章をWord形式に変換

```bash
chmod +x scripts/convert_chapters_to_word.sh
./scripts/convert_chapters_to_word.sh
```

### ステップ3: Wordファイルを結合

```bash
python3.11 scripts/merge_word_files.py
```

### ステップ4: 見出し構造を確認

```bash
python3.11 scripts/verify_word_structure.py
```

### ステップ5: Wordで最終調整

1. `complete_manuscript_v18_final.docx`をWordで開く
2. 目次を更新: 目次を右クリック → 「フィールドの更新」
3. ページ番号を設定: 「ページ番号の書式設定」→ 開始番号を1に設定
4. 最終確認: 誤字脱字、フォーマットの確認

### ステップ6: Amazon KDPに提出

1. [Amazon KDP](https://kdp.amazon.co.jp/)にログイン
2. 「新しい本を作成」をクリック
3. 「Kindle本の詳細」を入力
4. 「Kindle本のコンテンツ」で`complete_manuscript_v18_final.docx`をアップロード
5. プレビューを確認
6. 「保存して続行」をクリック

## トラブルシューティング

### 問題: Pandocが一部の見出しを認識しない

**解決策**: 章ごとに個別変換してから結合する（本スクリプト集で採用）

### 問題: 「第3部：実践編」がHeading 1として認識される

**解決策**: chapter6_final.mdの「# 第3部：実践編」を「## 第3部：実践編」に変更

### 問題: python-docxでの結合時にフォーマットが崩れる

**解決策**: すべての章で同じ参照用Word文書（`complete_manuscript_v10.docx`）を使用

## 参考資料

- [Amazon KDP用Word文書の仕様定義](../docs/amazon_kdp_word_specification.md)
- [マークダウンからWord文書への変換プロセス](../docs/conversion_process.md)
- [試行錯誤の記録と解決策](../docs/troubleshooting_history.md)

## バージョン履歴

| バージョン | 日付 | 変更内容 |
|:---|:---|:---|
| v1.0 | 2025-12-04 | 初版作成 |
