# AI旅行本プロジェクト README

**最終更新日**: 2025-12-05

---

## ⚠️ 最重要事項（必ず読むこと）

### 章ごとのマークダウンファイルが最新のベース

**重要**: 本プロジェクトでは、**章ごとのマークダウンファイル**が最新のベースであり、すべての修正はこれらのファイルに対して行う必要があります。

#### 章ごとのファイル一覧（`finals/`ディレクトリ）

1. `title_page_final.png` - 扉（タイトルページ画像）
2. `title_page_text_v1.md` - 扉（テキスト） | [🔗 Notion](https://www.notion.so/2c0004ae5e3581dbb1b4d4ba92554b36)
3. `halftitle_v1.md` - 中扉 | [🔗 Notion](https://www.notion.so/2c0004ae5e3581b9942ccdf499f2d7fd)
4. `disclaimer_v2.md` - ディスクレイマー | [🔗 Notion](https://www.notion.so/2c0004ae5e3581699f09e467783c1d1e)
5. `quickstart.md` - クイックスタートガイド
6. `preface.md` - はじめに | [🔗 Notion](https://www.notion.so/2c0004ae5e358111abfacc20e9134cf8)
7. `chapter1_final.md` - 第1章 | [🔗 Notion](https://www.notion.so/2c0004ae5e35817b9be7fc84bb00dbce)
8. `chapter2_final.md` - 第2章 | [🔗 Notion](https://www.notion.so/2c0004ae5e35817b9ba1dcb24cb8a94a)
9. `chapter3_final.md` - 第3章 | [🔗 Notion](https://www.notion.so/2c0004ae5e3581ad9ad5eba6ff9f6fff)
10. `chapter4_final.md` - 第4章 | [🔗 Notion](https://www.notion.so/2c0004ae5e35818eb287e23244033de3)
11. `chapter5_final.md` - 第5章 | [🔗 Notion](https://www.notion.so/2c0004ae5e35811ab09edc573d98cfdb)
12. `chapter6_final.md` - 第6章 | [🔗 Notion](https://www.notion.so/2c0004ae5e3581d096c7e8af69f200eb)
13. `chapter7_final.md` - 第7章 | [🔗 Notion](https://www.notion.so/2c0004ae5e358143b18eef4c3a542484)
14. `chapter8_final.md` - 第8章 | [🔗 Notion](https://www.notion.so/2c0004ae5e358180bfcad3341df60887)
15. `chapter9_final.md` - 第9章 | [🔗 Notion](https://www.notion.so/2c0004ae5e3581368110c1b65e7b003f)
16. `chapter10_final.md` - 第10章 | [🔗 Notion](https://www.notion.so/2c0004ae5e3581849defe9ffad49f99f)
17. `chapter11_final.md` - 第11章 | [🔗 Notion](https://www.notion.so/2c0004ae5e35816bb1e8f43607477967)
18. `chapter12_final.md` - 第12章 | [🔗 Notion](https://www.notion.so/2c0004ae5e3581009c26d1ca5e7dcf48)
19. `afterword.md` - おわりに
20. `colophon_v2.md` - 奥付 | [🔗 Notion](https://www.notion.so/2c0004ae5e358197b9d7ed648160e648)
21. `appendix_a_final.md` - 付録A（WEB限定）
22. `appendix_b_final.md` - 付録B | [🔗 Notion](https://www.notion.so/2c0004ae5e3581fbbc5dd0030cbb2a6e)
23. `appendix_c_final.md` - 付録C | [🔗 Notion](https://www.notion.so/2c0004ae5e35818cb2b7e5f0762279af)

#### バージョン管理の方法

章ごとのファイルは、以下の方法でバージョン管理されています：

1. **統合マークダウンファイルを章ごとに分割して保存**
   - 例：`complete_manuscript_v16.md` → `v16_part_00_quickstart.md`, `v16_part_01_preface.md`, `v16_part_02_chapter01.md`, ...
   - 命名規則：`v{バージョン番号}_part_{章番号}_{章名}.md`
   - 保存場所：`finals/`ディレクトリ

2. **最新の章ごとのファイルを修正する際の手順**
   - 修正前に、現在のバージョンを`v{番号}_part_*`として保存
   - 章ごとのファイル（`chapter1_final.md`など）を修正
   - 統合マークダウンとWord文書を再生成

3. **バージョンの確認方法**
   - `finals/`ディレクトリで`ls -lh v*_part_*.md`を実行
   - 最新のバージョン番号を確認

4. **バージョン管理の注意事項**
   - 章ごとのファイルを修正する前に、必ずバージョンを保存する
   - バージョン番号は連続して付ける（v16, v17, v18, ...）
   - バージョンごとの分割ファイルは削除しない

#### 絶対に守るべきルール

1. **修正は必ず章ごとのファイルに対して行う**
   - 統合マークダウン（`complete_manuscript_vXX.md`）やWord文書（`complete_manuscript_vXX_final.docx`）は、章ごとのファイルから生成される
   - 統合ファイルを直接修正しても、次回の生成時に失われる

2. **章ごとのファイルを上書きする前に必ずバックアップを取る**
   - 特に、古いバージョンからの復元を行う場合は注意

3. **Word文書の生成プロセス**
   
   **前提条件**: 参照用Word文書（`complete_manuscript_v10.docx`）が`finals/`ディレクトリに存在すること
   - 参照文書は、Amazon KDP用のフォーマット（ヘッダー、フッター、ページサイズ、余白）を提供します
   - サンプル参照文書は`standards/amazon_kdp/reference_document_sample.docx`にあります
   
   ```bash
   # ステップ1: 各章をWord形式に変換
   ./scripts/amazon_kdp/convert_chapters_to_word.sh
   
   # ステップ2: Wordファイルを結合
   python3.11 scripts/amazon_kdp/merge_word_files.py
   
   # ステップ3: 見出し構造を確認
   python3.11 scripts/amazon_kdp/verify_word_structure.py
   ```

4. **統合マークダウンの生成プロセス**
   ```bash
   # 章ごとのファイルを結合
   ./scripts/amazon_kdp/create_combined_markdown.sh
   ```

#### よくある間違い

- ✗ 統合マークダウンを修正して、それを章ごとに分割する
- ✗ Word文書を修正して、それをマークダウンに逆変換する
- ✗ 古いバージョンの統合ファイルから章ごとのファイルを上書きする（最新の修正が失われる）

#### 正しいワークフロー

1. 章ごとのファイルを修正
2. 統合マークダウンを生成（必要に応じて）
3. Word文書を生成
4. 見出し構造を確認
5. 問題があれば、**ステップ1に戻って章ごとのファイルを修正**

---

## 1. プロジェクト憲章

### 1.1. プロジェクト名
『僕の旅の相棒は、ChatGPTでした。 - AIと共に働き、生きる時代の思考法』執筆プロジェクト

### 1.2. プロジェクトの目的
本書を通じて、ビジネスパーソンがAIを単なる「道具」としてではなく、思考を深め、世界を広げる「相棒」として活用するための新しい思考法と実践術を提示する。

### 1.3. プロジェクトのゴール
- 書籍の完成・出版
- AIとの協業による新しい執筆プロセスの確立

### 1.4. プロジェクトのスコープ
- 書籍の企画、執筆、編集、校正
- 関連ドキュメントの作成・管理

---

## 2. マスタープラン（書籍構成）

本書は以下の4部構成、全12章で構成される。

- **第1部：AIとの出会い**
  - 第1章：なぜ今、あなたの旅に「AIという相棒」が必要なのか？
  - 第2章：本書を120%楽しむための「読み方」ガイド
- **第2部：AIは「完璧な旅の設計士」である**
  - 第3章：完璧な旅の設計士
  - 第4章：最強の現場司令塔
  - 第5章：冷静な危機管理コンサルタント
- **第3部：AIと共に、混沌のベトナムを旅する**
  - 第6章：ホーチミン - 混沌の中の秩序
  - 第7章：旅行中に使える「実践プロンプト集」
  - 第8章：トラブル対応の「緊急プロンプト集」
  - 第9章：旅行後の振り返りに使える「分析プロンプト集」
- **第4部：AIと描く、旅の未来地図**
  - 第10章：AI旅行の光と影
  - 第11章：AI時代の旅行者に求められる3つのスキル
  - 第12章：あなたの旅を変える第一歩
- **巻末付録**
  - 付録A：AIとの対話ログ集（購入者限定WEB付録）
  - 付録B：プロンプトテンプレート集
  - 付録C：AIツール総合ガイド

---

## 3. 企画・設計ドキュメント

本プロジェクトの企画・設計段階で作成した重要なドキュメントは、`planning/`ディレクトリに格納されています。

### 3.1. 主要な企画ドキュメント

| ドキュメント | 内容 | ファイルパス | Notion |
|:---|:---|:---|:---|
| 書籍企画書 | プロジェクトの目的、ターゲット読者、差別化ポイント | planning/book_proposal.md | [🔗 Notion](https://www.notion.so/2c0004ae5e3581cb966befa674f3acd3) |
| 章構成マップ | 全体の章立てと各章の役割 | planning/chapter_structure_map.md | [🔗 Notion](https://www.notion.so/2c0004ae5e35810bbf50d6efd4cad152) |
| ターゲット読者ペルソナ | メインペルソナとサブペルソナの詳細 | planning/target_reader_persona.md | [🔗 Notion](https://www.notion.so/2c0004ae5e3581199015d81dec827e07) |
| 市場調査 | 市場規模、ターゲット市場、購買動機 | planning/market_research.md | [🔗 Notion](https://www.notion.so/2c0004ae5e3581e9bf88c6c19846ec8b) |
| 競合分析 | 競合書籍の分析と差別化ポイント | planning/competitive_analysis.md | [🔗 Notion](https://www.notion.so/2c0004ae5e3581abb4e3d11072efd30d) |
| 役割分担表 | WBSに基づくフェーズ別役割分担 | planning/role_breakdown_by_phase.md | [🔗 Notion](https://www.notion.so/2c0004ae5e358124b22ccd9fbcf39b19) |

### 3.2. プロジェクト管理ドキュメント

| ドキュメント | 内容 | ファイルパス | Notion |
|:---|:---|:---|:---|
| 進捗報告 | 最新のプロジェクト進捗状況 | project_management/progress_report_v11.md | [🔗 Notion](https://www.notion.so/2c0004ae5e358128830bed1a3c1828f8) |
| 課題管理 | 現在の課題と対応状況 | project_management/issue_tracker_v4.md | [🔗 Notion](https://www.notion.so/2c0004ae5e3581dea642ca3ef5d4875d) |
| WBS | 作業分解構造図（最新版） | planning/wbs_v13.md | — |

---

## 4. 進捗ダッシュボード

| 章 | タイトル | ステータス | 最新版ファイル |
| :-- | :--- | :--- | :--- |
| - | 扉（タイトルページ） | ✅ 完了 | finals/title_page_final.png, finals/title_page_text_v1.md |
| - | 中扉 | ✅ 完了 | finals/halftitle_v1.md |
| - | ディスクレイマー | ✅ 完了 | finals/disclaimer_v2.md |
| - | はじめに | ✅ 完了 | finals/preface.md |
| 1 | なぜ今、あなたの旅に「AIという相棒」が必要なのか？ | ✅ 完了 | finals/chapter1_final.md |
| 2 | 本書を120%楽しむための「読み方」ガイド | ✅ 完了 | finals/chapter2_final.md |
| 3 | 完璧な旅の設計士 | ✅ 完了 | finals/chapter3_final.md |
| 4 | 最強の現場司令塔 | ✅ 完了 | finals/chapter4_final.md |
| 5 | 冷静な危機管理コンサルタント | ✅ 完了 | finals/chapter5_final.md |
| 6 | ホーチミン - 混沌の中の秩序 | ✅ 完了 | finals/chapter6_final.md |
| 7 | 旅行中に使える「実践プロンプト集」 | ✅ 完了 | finals/chapter7_final.md |
| 8 | トラブル対応の「緊急プロンプト集」 | ✅ 完了 | finals/chapter8_final.md |
| 9 | 旅行後の振り返りに使える「分析プロンプト集」 | ✅ 完了 | finals/chapter9_final.md |
| 10 | AI旅行の光と影 | ✅ 完了 | finals/chapter10_final.md |
| 11 | AI時代の旅行者に求められる3つのスキル | ✅ 完了 | finals/chapter11_final.md |
| 12 | あなたの旅を変える第一歩 | ✅ 完了 | finals/chapter12_final.md |
| - | おわりに | ✅ 完了 | finals/afterword.md |
| - | 奥付 | ✅ 完了 | finals/colophon_v2.md |
| A | AIとの対話ログ集（WEB限定） | ✅ 完了（拡充版） | finals/appendix_a_final.md |
| B | プロンプトテンプレート集 | ✅ 完了 | finals/appendix_b_final.md |
| C | AIツール総合ガイド | ✅ 完了 | finals/appendix_c_final.md |
| - | 統合原稿v29（最新版） | ✅ 完了 | finals/complete_manuscript_v29.md |
| - | 統合原稿v18（Word版） | ✅ 完了 | finals/complete_manuscript_v18_final.docx |

**全体進捗率**: 100%（執筆タスク完了、出版前対応準備中）

---

## 5. 最終成果物

### 4.1. 統合原稿

#### 4.1.1. 統合原稿v29（最新版）
- **ファイル名**: `finals/complete_manuscript_v29.md`
- **文字数**: 192,837文字
- **行数**: 8,511行
- **構成**: はじめに + 第1章〜第12章 + おわりに + 付録B・C
- **作成日**: 2025年11月27日
- **状態**: 改善提案①②③完了、出版前対応準備中

### 4.2. 付録A（購入者限定WEB付録）

#### 4.2.1. 付録A拡充版（最新版）
- **ファイル名**: `log_coverage_improvement/appendix_a_expanded.md`
- **文字数**: 約1.4MB
- **収録ログ**: LOG001〜LOG051（37件）
- **特徴**: 各LOGに4つの解説（なぜこのプロンプトを使ったか、結果の評価、改善点、読者へのアドバイス）を追加
- **公開方法**: 購入者限定WEBサイト

#### 4.2.2. 付録A（旧版）
- **ファイル名**: `drafts/appendix_a_final.md`
- **文字数**: 61,602文字
- **収録ログ**: LOG001〜LOG019（19件）

### 4.3. 総文字数
- **統合原稿v29（本文 + 付録B・C）**: 約430KB
- **付録A拡充版（WEB限定）**: 約1.4MB
- **合計**: 約1.6MB

---

## 5. プロジェクトの進め方

### 5.1. 最優先事項：WBSに従うこと

本プロジェクトのすべての作業は、**最新のWBS** に基づいて進められます。WBSは本プロジェクトの「法律」であり、すべての作業内容、手順、担当者、工数が定義されています。作業を開始する前、または作業内容に疑問が生じた場合は、必ずWBSを参照してください。

### 5.2. 標準作業手順書 (SOP)

本プロジェクトで採用されている執筆ワークフロー、品質管理基準、ファイル管理規則などの標準的な手順は、以下の「執筆業務標準化ドキュメント」にまとめられています。WBSを理解する上での前提知識となりますので、必ず一読してください。

- [執筆業務標準化ドキュメント (SOP)](./standards/document_creation_guideline.md)

### 5.3. WBSの運用ルール

WBSを更新する際は、以下の手順に従ってください。

1.  `wbs_latest.md`をコピーし、新しいバージョン番号を付けて保存します。（例: `wbs_v10.md`）
2.  `wbs_latest.md`を直接編集します。
3.  変更内容をコミットし、関係者に通知します。

---

## 6. 関連ドキュメント

### 6.1. 本プロジェクト固有のドキュメント

- **最新のWBS**: [planning/wbs_latest.md](./planning/wbs_latest.md)
- **書籍企画書**: [planning/book_proposal.md](./planning/book_proposal.md)
- **章構成マップ**: [planning/chapter_structure_map.md](./planning/chapter_structure_map.md)
- **プロジェクト専用ガイドライン**: [standards/project_specific_guideline.md](./standards/project_specific_guideline.md)
- **最新進捗報告**: [project_management/progress_report_v9.md](./project_management/progress_report_v9.md)

### 6.2. 執筆業務標準化ドキュメント

- **汎用ドキュメント作成ガイドライン**: [standards/document_creation_guideline.md](./standards/document_creation_guideline.md)
- **Amazon KDP用Word文書作成ガイド**: [standards/amazon_kdp/README.md](./standards/amazon_kdp/README.md)

### 6.3. 最終成果物

- **統合原稿**: [finals/complete_manuscript.md](./finals/complete_manuscript.md)
- **付録A（WEB限定）**: [drafts/appendix_a_final.md](./drafts/appendix_a_final.md)
- **付録B**: [finals/appendix_b_final.md](./finals/appendix_b_final.md)
- **付録C**: [finals/appendix_c_final.md](./finals/appendix_c_final.md)

---

## 7. 出版準備要件

### 7.1. Word化の要件

最終的な出版形式は、**Microsoft Word形式（.docx）**とし、以下の要件に従って変換・整形を行う。

#### 7.1.1. 見出し構造

- **Wordのアウトライン機能を使用**して、章・節・項を構造化する
  - Markdownの `#`（章タイトル） → Wordの「見出し1」
  - Markdownの `##`（節） → Wordの「見出し2」
  - Markdownの `###`（項） → Wordの「見出し3」
- Wordのアウトライン機能を使って、自動的に目次を生成する

#### 7.1.2. 装飾・書式

- Markdown形式の装飾（`**太字**`、`*斜体*`など）は使用しない
- すべての装飾はWordのスタイル機能で管理する
- フォント、行間、余白などは参考書籍（野沢温泉探訪記）に準拠

#### 7.1.3. 参考書籍

- **ファイル名**: `野沢温泉探訪記～世界が注目する村の魅力と地域戦略のリアル第２版ｘサイズ調整.docx`
- **保存場所**: `/home/ubuntu/upload/`
- この書籍のレイアウト、見出しスタイル、目次形式を参考にする

#### 7.1.4. PDF化

- Word形式で完成した原稿をPDF化し、Amazon KDPにアップロードする
- PDFのページサイズ、余白は参考書籍に準拠

---

## 8. プロジェクト管理

### 7.1. プロジェクトオーナー
浅見純一郎

### 7.2. 執筆支援AI
Manus

---

## 9. 次のステップ

### 8.1. 改善提案の実施状況（✅ 完了）
- 改善提案②「クイックスタートガイドの追加」：✅ 完了（v12で実装）
- 改善提案①「第3部と付録Bの重複感の解消」：✅ 完了（v13で実装、28箇所）
- v29まで継続的に改善・更新
- 改善提案③「LOG網羅性の向上」：✅ 完了（付録Aを19件→37件に拡充）

### 8.2. 付録AのWEBアップロード
- 実際のURLを設定
- QRコードを生成
- 「おわりに」と「第2章」のダミーURLを実際のURLに置き換え

### 8.3. ユーザー最終確認
- 統合原稿の最終確認
- 誤字脱字のチェック
- 全体の流れの確認

### 8.4. Amazon KDP用Word文書の作成（✅ 完了）
- v29まで継続的にWord文書を更新
- Amazon KDP用Word文書作成プロセスをドキュメント化
- 再現可能なスクリプトを作成

### 8.5. 出版社への提出
- 統合原稿の提出
- 付録AのURL情報の提供

---

**プロジェクト完了予定日**: 2025年11月末

---

## 9. 筆者レビュー・編集作業の方針

### 9.1. 重要：編集作業フローを必ず確認すること

⚠️ **編集作業を開始する前に、必ず以下のドキュメントを読んでください**：

- **[編集作業フロー](./EDITING_WORKFLOW.md)** ← **必読！**

このドキュメントには、以下の重要なルールが記載されています：

1. **各章ファイルを編集の基本単位とする**（統合原稿を直接編集しない）
2. **複数カテゴリーの編集は一度にまとめて実施する**（個別に実施しない）

### 9.2. 基本方針

- **編集対象**: 各章ごとのドキュメント（`finals/chapter*_final.md`、`finals/introduction_final.md`、`finals/conclusion_final.md`など）
- **統合原稿は直接編集しない**: 各章を修正後、最後に統合原稿を生成
- **作業順序**: すべてのカテゴリーの調査レポートを完成させてから、一度に編集を実施

### 9.2. 作業カテゴリー

| カテゴリー | 説明 | 工数 |
|-----------|------|------|
| **A. 即座対応可能** | 機械的な置換・削除・追加 | 12.8時間 |
| **B. 調査が必要** | ログ確認、内容検証、事実確認 | 6時間 |
| **C. 検討が必要** | 筆者との方針決定、表現調整、構成変更 | 6時間 |

**合計工数**: 24.8時間

### 9.3. 関連ドキュメント

- **編集作業フロー**: [EDITING_WORKFLOW.md](./EDITING_WORKFLOW.md) ← **必読！**
- **詳細編集計画書**: [reviews/editorial_plan_v4_detailed.md](./reviews/editorial_plan_v4_detailed.md)
- **筆者コメント集**: [reviews/user_comments_collection.md](./reviews/user_comments_collection.md)
- **WBS v11**: [planning/wbs_v11.md](./planning/wbs_v11.md)
- **カテゴリーA調査レポート**: [reviews/category_a_investigation_report.md](./reviews/category_a_investigation_report.md)
- **カテゴリーB調査レポート**: [reviews/category_b_investigation_report.md](./reviews/category_b_investigation_report.md)
- **カテゴリーC調査レポート**: [reviews/category_c_investigation_report.md](./reviews/category_c_investigation_report.md)
