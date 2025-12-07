# 編集作業フロー

このドキュメントは、AI旅行書籍の編集作業を効率的に進めるためのフローとルールを定義します。

---

## 基本原則

### 原則1：各章ファイルを編集の基本単位とする

**❌ やってはいけないこと**：
- 統合原稿（`complete_manuscript_vX.md`）に対して直接編集する

**✅ 正しい方法**：
- 各章のファイル（`chapter1_final.md`、`chapter2_final.md`等）に対して編集する
- 編集完了後、各章ファイルを統合して統合原稿を作成する

**理由**：
- 各章ファイルが編集の「マスターデータ」である
- 統合原稿は各章ファイルから生成される「派生データ」である
- 統合原稿を直接編集すると、次回の統合時に変更が失われる

---

### 原則2：複数カテゴリーの編集は一度にまとめて実施する

**❌ やってはいけないこと**：
- カテゴリーA、B、Cを個別に実施し、その都度統合原稿を作成する

**✅ 正しい方法**：
1. すべてのカテゴリー（A、B、C等）の調査レポートを完成させる
2. すべての変更内容を確認・承認する
3. 各章ファイルに対して、すべてのカテゴリーの編集を一度に実施する
4. 編集完了後、各章ファイルを統合して統合原稿を作成する

**理由**：
- 統合作業は時間がかかるため、何度も繰り返すのは非効率
- 各カテゴリーの変更が相互に影響する可能性がある
- 一度にまとめて実施することで、全体の整合性を保ちやすい

---

## 編集作業の標準フロー

### フェーズ1：調査・計画

1. **カテゴリー別の調査レポートを作成**
   - カテゴリーA（構成の整理）
   - カテゴリーB（内容の正確性）
   - カテゴリーC（表現の統一性）
   - その他のカテゴリー

2. **調査レポートのレビュー**
   - すべてのカテゴリーの調査レポートを完成させる
   - 変更内容を確認・承認する
   - 変更の優先順位を決定する

3. **編集計画の作成**
   - どの章にどのような変更を加えるかを明確にする
   - 変更箇所の一覧を作成する
   - 作業の順序を決定する

### フェーズ2：編集実施

4. **各章ファイルに対して編集を実施**
   - `introduction_final.md`（はじめに）
   - `chapter1_final.md`（第1章）
   - `chapter2_final.md`（第2章）
   - ...
   - `chapter12_final.md`（第12章）
   - `conclusion_final.md`（おわりに）
   - `appendix_final.md`（付録）

5. **編集内容の検証**
   - 各章ファイルの変更内容を確認
   - 誤字脱字のチェック
   - 表記の統一性の確認

### フェーズ3：統合・検証

6. **統合原稿の作成**
   - 各章ファイルを統合して統合原稿を作成
   - ファイル名: `complete_manuscript_vX.md`（Xはバージョン番号）

7. **統合原稿の検証**
   - 章の順序が正しいか確認
   - 章間の接続が自然か確認
   - 全体の整合性を確認

8. **変更完了レポートの作成**
   - 実施した変更内容をまとめる
   - 変更箇所の一覧を作成する
   - 統計情報（行数、変更箇所数等）を記録する

---

## ファイル構成

### 編集対象ファイル（マスターデータ）

```
/home/ubuntu/ai_travel_book_project/finals/
├── introduction_final.md    # はじめに
├── chapter1_final.md         # 第1章
├── chapter2_final.md         # 第2章
├── chapter3_final.md         # 第3章
├── chapter4_final.md         # 第4章
├── chapter5_final.md         # 第5章
├── chapter6_final.md         # 第6章
├── chapter7_final.md         # 第7章
├── chapter8_final.md         # 第8章
├── chapter9_final.md         # 第9章
├── chapter10_final.md        # 第10章
├── chapter11_final.md        # 第11章
├── chapter12_final.md        # 第12章
├── conclusion_final.md       # おわりに
└── appendix_final.md         # 付録
```

### 統合原稿（派生データ）

```
/home/ubuntu/ai_travel_book_project/finals/
├── complete_manuscript_v1.md  # 初版
├── complete_manuscript_v2.md  # カテゴリーA編集後
├── complete_manuscript_v3.md  # カテゴリーB編集後
└── complete_manuscript_v4.md  # カテゴリーC編集後
```

### 調査レポート

```
/home/ubuntu/ai_travel_book_project/reviews/
├── category_a_investigation_report.md  # カテゴリーA調査レポート
├── category_b_investigation_report.md  # カテゴリーB調査レポート
└── category_c_investigation_report.md  # カテゴリーC調査レポート
```

### 変更完了レポート

```
/home/ubuntu/ai_travel_book_project/reports/
├── category_a_completion_report.md  # カテゴリーA変更完了レポート
├── category_b_completion_report.md  # カテゴリーB変更完了レポート
└── category_c_completion_report.md  # カテゴリーC変更完了レポート
```

---

## 統合原稿の作成方法

### コマンド

```bash
cd /home/ubuntu/ai_travel_book_project/finals

cat introduction_final.md \
    chapter1_final.md \
    chapter2_final.md \
    chapter3_final.md \
    chapter4_final.md \
    chapter5_final.md \
    chapter6_final.md \
    chapter7_final.md \
    chapter8_final.md \
    chapter9_final.md \
    chapter10_final.md \
    chapter11_final.md \
    chapter12_final.md \
    conclusion_final.md \
    appendix_final.md \
    > complete_manuscript_vX.md
```

### 注意事項

- バージョン番号（X）は、前回のバージョンから1つ増やす
- 統合前に各章ファイルの編集が完了していることを確認する
- 統合後、統合原稿の行数を確認する（`wc -l complete_manuscript_vX.md`）

---

## チェックリスト

### 編集開始前

- [ ] すべてのカテゴリーの調査レポートが完成している
- [ ] 変更内容が確認・承認されている
- [ ] 編集計画が作成されている
- [ ] 各章ファイルのバックアップが取られている

### 編集中

- [ ] 各章ファイルに対して編集している（統合原稿に対して編集していない）
- [ ] 変更内容を記録している
- [ ] 定期的に変更内容を確認している

### 編集完了後

- [ ] すべての各章ファイルの編集が完了している
- [ ] 各章ファイルの変更内容を検証している
- [ ] 統合原稿を作成している
- [ ] 統合原稿の検証を実施している
- [ ] 変更完了レポートを作成している

---

## よくある間違いと対策

### 間違い1：統合原稿に対して直接編集してしまう

**対策**：
- 編集前に、このドキュメントを必ず確認する
- 各章ファイルのパスを確認してから編集を開始する

### 間違い2：カテゴリーごとに個別に編集してしまう

**対策**：
- すべてのカテゴリーの調査レポートが完成するまで編集を開始しない
- 編集計画を作成し、すべての変更内容を一覧化する

### 間違い3：編集内容を記録していない

**対策**：
- 編集開始前に変更完了レポートのテンプレートを作成する
- 編集中に変更内容を随時記録する

---

## バージョン管理

### バージョン番号の付け方

- **v1**: 初版（各章ファイルを統合したもの）
- **v2**: カテゴリーA編集後
- **v3**: カテゴリーB編集後
- **v4**: カテゴリーA、B、C編集後
- **v5**: 最終版

### バージョン履歴

| バージョン | 作成日 | 変更内容 |
|----------|--------|---------|
| v1 | 2025-11-XX | 初版 |
| v2 | 2025-11-XX | カテゴリーA編集 |
| v3 | 2025-11-XX | カテゴリーB編集 |
| v4 | 2025-11-27 | カテゴリーC編集 |

---

## 参考資料

- [README.md](README.md): プロジェクト全体の概要
- [カテゴリーA調査レポート](reviews/category_a_investigation_report.md)
- [カテゴリーB調査レポート](reviews/category_b_investigation_report.md)
- [カテゴリーC調査レポート](reviews/category_c_investigation_report.md)

---

**作成日**: 2025年11月27日  
**最終更新**: 2025年11月27日  
**作成者**: AI（Manus）
