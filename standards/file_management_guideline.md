# ファイル管理ガイドライン

## 1. ディレクトリ構造

```
/home/ubuntu/ai_travel_book_project/
├── checklists/       # 詳細設計書との照合チェックリスト
├── drafts/           # 各章のドラフト
├── final/            # 各章の最終稿
├── materials/        # 執筆に必要な素材
│   ├── chapters/     # 章ごとの素材ファイル
│   └── giant_material_database.md # 全ログのデータベース
├── planning/         # プロジェクト計画関連
│   ├── detailed_designs/ # 各章の詳細設計書
│   ├── book_proposal.md # 書籍企画書
│   ├── chapter_structure_map.md # 章構成マップ
│   └── wbs_latest.md # 最新のWBS
├── reports/          # 各種報告書
├── reviews/          # 各種レビュー結果
├── scripts/          # 各種スクリプト
└── standards/        # 各種ガイドライン
```


## 2. ファイル命名規則

### 2.1. 基本ルール

- **英数字とアンダースコアを使用**: `chapter1_draft_v1.md`
- **スペースは使用しない**: `chapter 1 draft v1.md` → `chapter1_draft_v1.md`
- **バージョン番号を付与**: `_v1`, `_v2`
- **ステータスを付与**: `_draft`, `_final`

### 2.2. 具体例

- **ドラフト**: `chapter1_draft_v1.md`
- **最終稿**: `chapter1_final.md`
- **レビュー報告書**: `chapter1_editor_review_round1.md`
- **詳細設計書**: `chapter1_detailed_design_v1.md`

## 3. バージョン管理

- **メジャーバージョン**: 大幅な変更があった場合（例: `_v1` → `_v2`）
- **マイナーバージョン**: 軽微な修正があった場合（例: `_v1.1`）
- **最新版**: `_latest` を使用（例: `wbs_latest.md`）
