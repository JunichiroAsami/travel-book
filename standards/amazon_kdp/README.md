# Amazon KDP用Word文書作成ガイド

**最終更新日**: 2025年12月4日

## 概要

このドキュメントパッケージは、章ごとのマークダウンファイルからAmazon Kindle Direct Publishing (KDP)用のWord文書を作成するための完全なガイドです。

本書「AI旅行術」の制作過程で得られた知見を基に、再現可能なプロセスとスクリプトを提供します。

## ドキュメント構成

### 1. [Amazon KDP用Word文書の仕様定義](amazon_kdp_word_specification.md)

Amazon KDPに提出するWord文書の仕様を定義します。

**内容**:
- 文書構造（必須セクション、見出しレベル）
- フォーマット要件（フォント、行間、余白、ページ番号）
- マークダウンからの変換要件
- ファイル構成
- Amazon KDPの推奨事項
- 検証チェックリスト

**対象読者**: Amazon KDPに提出するWord文書の仕様を理解したい方

### 2. [マークダウンからWord文書への変換プロセス](conversion_process.md)

章ごとのマークダウンファイルからAmazon KDP用Word文書を作成する具体的なプロセスを説明します。

**内容**:
- 前提条件（必要なソフトウェア、ファイル構成）
- プロセス全体の流れ
- ステップ1: 各章を個別にPandocでWord変換
- ステップ2: 17個のWordファイルを結合
- ステップ3: 目次の更新とページ番号の設定
- ステップ4: 検証
- ステップ5: Amazon KDPに提出
- トラブルシューティング

**対象読者**: 実際にWord文書を作成する方

### 3. [試行錯誤の記録と解決策](troubleshooting_history.md)

Word文書作成過程で遭遇した問題と、その解決策を時系列で記録します。

**内容**:
- 問題1: v16がv13の変更内容を反映していない
- 問題2: Pandocで大きなファイルを変換すると一部の見出しが認識されない
- 問題3: 「第3部：実践編」がHeading 1として認識される
- 問題4: Pandocが「**本章の使い方**：」を誤認識
- 問題5: python-docxでの結合時にフォーマットが崩れる
- 学んだ教訓

**対象読者**: 同様の問題に遭遇した方、プロセスの背景を理解したい方

## スクリプト集

[../scripts/](../scripts/)ディレクトリには、以下のスクリプトが含まれています：

### 1. create_combined_markdown.sh

章ごとのマークダウンファイルを結合して統合マークダウンファイルを作成します。

### 2. convert_chapters_to_word.sh

各章のマークダウンファイルをPandocでWord形式に変換します。

### 3. merge_word_files.py

17個のWordファイルを結合してAmazon KDP用の完成版を作成します。

### 4. verify_word_structure.py

Word文書の見出し構造を確認します。

詳細は[../scripts/README.md](../scripts/README.md)を参照してください。

## クイックスタート

### 前提条件

1. **Pandoc** (バージョン 2.0以降)
   ```bash
   pandoc --version
   ```

2. **Python 3.11** (python-docxライブラリ)
   ```bash
   python3.11 --version
   pip3 install python-docx
   ```

3. **参照用Word文書** (スタイル定義用)
   - 本プロジェクトに含まれるサンプル: `reference_document_sample.docx`
   - 本書の場合: `complete_manuscript_v10.docx`
   
   **参照文書について**:
   - Pandocの`--reference-doc`オプションで使用
   - ヘッダー、フッター、余白、フォントなどのスタイル情報を提供
   - `reference_document_sample.docx`は最初の2章のみを含む軽量版（スタイル情報は完全に保持）

### 手順

#### ステップ1: 各章をWord形式に変換

```bash
cd /home/ubuntu/ai_travel_book_project/finals
chmod +x scripts/convert_chapters_to_word.sh
./scripts/convert_chapters_to_word.sh
```

#### ステップ2: Wordファイルを結合

```bash
python3.11 scripts/merge_word_files.py
```

#### ステップ3: 見出し構造を確認

```bash
python3.11 scripts/verify_word_structure.py
```

#### ステップ4: Wordで最終調整

1. `complete_manuscript_v18_final.docx`をWordで開く
2. 目次を更新: 目次を右クリック → 「フィールドの更新」
3. ページ番号を設定: 「ページ番号の書式設定」→ 開始番号を1に設定
4. 最終確認: 誤字脱字、フォーマットの確認

#### ステップ5: Amazon KDPに提出

1. [Amazon KDP](https://kdp.amazon.co.jp/)にログイン
2. 「新しい本を作成」をクリック
3. 「Kindle本のコンテンツ」で`complete_manuscript_v18_final.docx`をアップロード
4. プレビューを確認
5. 「保存して続行」をクリック


## ファイル構成

```
/home/ubuntu/ai_travel_book_project/
├── standards/amazon_kdp/                    # Amazon KDP用ドキュメント
│   ├── README.md                            # このファイル
│   ├── amazon_kdp_word_specification.md     # Amazon KDP用Word文書の仕様定義
│   ├── conversion_process.md                # マークダウンからWord文書への変換プロセス
│   ├── troubleshooting_history.md           # 試行錯誤の記録と解決策
│   └── reference_document_sample.docx       # 参照用Word文書（サンプル）
├── scripts/amazon_kdp/                      # スクリプト集
│   ├── README.md                            # スクリプトのREADME
│   ├── create_combined_markdown.sh          # 統合マークダウンファイルを作成
│   ├── convert_chapters_to_word.sh          # 各章をWord形式に変換
│   ├── merge_word_files.py                  # Wordファイルを結合
│   └── verify_word_structure.py             # Word文書の見出し構造を確認
├── finals/                                  # 章ごとのマークダウンファイル
│   ├── quickstart.md                        # クイックスタートガイド
│   ├── preface.md                           # はじめに
│   ├── chapter1_final.md                    # 第1章
│   ├── chapter2_final.md                    # 第2章
│   ├── chapter3_final.md                    # 第3章
│   ├── chapter4_final.md                    # 第4章
│   ├── chapter5_final.md                    # 第5章
│   ├── chapter6_final.md                    # 第6章
│   ├── chapter7_final.md                    # 第7章
│   ├── chapter8_final.md                    # 第8章
│   ├── chapter9_final.md                    # 第9章
│   ├── chapter10_final.md                   # 第10章
│   ├── chapter11_final.md                   # 第11章
│   ├── chapter12_final.md                   # 第12章
│   ├── afterword.md                         # おわりに
│   ├── appendix_b_final.md                  # 付録B
│   ├── appendix_c_final.md                  # 付録C
│   ├── complete_manuscript_v21.md           # 統合マークダウンファイル
│   ├── complete_manuscript_v21_final.docx   # 完成版Word文書
│   └── complete_manuscript_v10.docx         # 参照用Word文書（フル版）
```

**参照文書について**:
- `reference_document_sample.docx`: 軽量版（最初の2章のみ、約60KB）
- `complete_manuscript_v10.docx`: フル版（全17章、約180KB）
- どちらもスタイル情報は同じ（ヘッダー、フッター、ページサイズ、余白など）
- Pandocの`--reference-doc`オプションで使用可能
├── appendix_b_final.md                      # 付録B
├── appendix_c_final.md                      # 付録C
├── complete_manuscript_v18.md               # 統合マークダウンファイル
├── complete_manuscript_v18_final.docx       # 完成版Word文書
└── complete_manuscript_v10.docx             # 参照用Word文書
```

## よくある質問

### Q1: なぜ章ごとに個別変換するのですか？

**A**: Pandocには大きなファイルを変換する際の制限があり、約1800行以降の見出しが正しく認識されない場合があります。章ごとに個別変換することで、この制限を回避できます。

### Q2: 参照用Word文書は必須ですか？

**A**: **必須**です。Amazon KDP用の正しいフォーマット（ヘッダー、フッター、ページサイズ、余白など）を適用するために必要です。本プロジェクトには`reference_document_sample.docx`が含まれています。これは最初の2章のみを含む軽量版ですが、スタイル情報は完全に保持されています。

### Q3: 統合マークダウンファイル（complete_manuscript_v18.md）は必要ですか？

**A**: 必須ではありません。Word変換には章ごとのファイルを使用するため、統合マークダウンファイルは参照用です。

### Q4: 水平線（---）は削除すべきですか？

**A**: 推奨します。Wordでは見出しの区切りが明確なため、水平線は不要です。また、Pandocが誤認識する可能性もあります。

### Q5: 目次は自動生成されますか？

**A**: はい。`convert_chapters_to_word.sh`では、最初のファイル（chapter_00.docx）のみ`--toc`オプションを使用して目次を自動生成します。ただし、Word文書を結合した後、Wordで「フィールドの更新」を実行する必要があります。

## トラブルシューティング

### 問題: Pandocが一部の見出しを認識しない

**解決策**: 章ごとに個別変換してから結合する（本プロセスで採用）

### 問題: 「第3部：実践編」がHeading 1として認識される

**解決策**: chapter6_final.mdの「# 第3部：実践編」を「## 第3部：実践編」に変更

### 問題: python-docxでの結合時にフォーマットが崩れる

**解決策**: すべての章で同じ参照用Word文書（`complete_manuscript_v10.docx`）を使用

詳細は[troubleshooting_history.md](troubleshooting_history.md)を参照してください。

## 参考資料

- [Amazon KDP ヘルプ - 原稿のフォーマット](https://kdp.amazon.co.jp/ja_JP/help/topic/G200645680)
- [Pandoc User's Guide](https://pandoc.org/MANUAL.html)
- [python-docx Documentation](https://python-docx.readthedocs.io/)

## バージョン履歴

| バージョン | 日付 | 変更内容 |
|:---|:---|:---|
| v1.0 | 2025-12-04 | 初版作成 |

## ライセンス

このドキュメントパッケージは、本書「AI旅行術」の制作過程で得られた知見を基に作成されています。

## お問い合わせ

質問や改善提案がある場合は、プロジェクトの管理者にお問い合わせください。
