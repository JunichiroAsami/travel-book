# 試行錯誤の記録と解決策

**最終更新日**: 2025年12月4日

## 概要

このドキュメントでは、章ごとのマークダウンファイルからAmazon KDP用Word文書を作成する過程で遭遇した問題と、その解決策を時系列で記録します。

## 問題1: v16がv13の変更内容を反映していない

### 発生日時
2025年12月4日

### 問題の詳細

**症状**:
- v16のマークダウンファイルには、v13で行われた28箇所の修正が反映されていない
- 具体的には、以下の内容が欠落：
  - 第6〜9章の冒頭に案内文
  - 第6〜9章の末尾に対応表
  - 付録Bの各テンプレートに「第3部での詳細解説」

**原因**:
- v16の元となったマークダウンファイルが、v13ではなく、v12またはそれ以前のバージョンだった
- 章ごとのファイル（chapter1_final.md〜chapter12_final.md）にもv13の変更内容が反映されていなかった

### 解決策

**ステップ1**: v13の変更内容を確認

v13の実装レポート（`v13_implementation_report.md`）から、28箇所の修正内容を抽出：

1. 第2章に「2.3. 第3部と付録Bの使い分け」を追加
2. 付録Bの冒頭に「第3部との違い」を追加
3. 第6〜9章の冒頭に案内文を追加
4. 第6〜9章の末尾に対応表を追加
5. 付録Bの各テンプレートに「第3部での詳細解説」を追加

**ステップ2**: 章ごとのファイルにv13の変更内容を反映

`update_chapter_files_with_v13_changes.py`を作成して、章ごとのファイルを更新：

```python
#!/usr/bin/env python3
"""
章ごとのファイルにv13の変更内容を反映
"""

def update_chapter6_to_9():
    """第6〜9章の冒頭に案内文、末尾に対応表を追加"""
    
    chapters = {
        'chapter6_final.md': '旅行前の準備',
        'chapter7_final.md': '旅行中の実践',
        'chapter8_final.md': 'トラブル対応',
        'chapter9_final.md': '旅行後の振り返り'
    }
    
    for filename, context in chapters.items():
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 冒頭に案内文を追加
        intro_text = """
**本章の使い方**

本章では、実際の旅行体験を通じて「なぜそのプロンプトを使ったのか」「どう改善したのか」を学べます。プロンプトをすぐに使いたい方は、**付録B**のテンプレート集をご参照ください。

---
"""
        
        # 末尾に対応表を追加
        outro_text = """

## 本章のプロンプトを今すぐ使いたい方へ

本章で紹介したプロンプトは、**付録B**でコピペ用テンプレートとして提供しています。以下の対応表から、該当するテンプレートを探してご活用ください。

| 本章のプロンプト | 付録Bの該当テンプレート |
|:---|:---|
| 本章で紹介した各プロンプト | 付録B「1. 旅行計画編」〜「4. 振り返り編」 |

**付録Bの使い方**：
1. 付録Bの目次から、使いたいテンプレートを探す
2. 【】内を自分の情報に置き換える
3. ChatGPTに入力する
"""
        
        # 見出しの直後に案内文を挿入
        content = content.replace(
            f'# 第{章番号}章：',
            f'# 第{章番号}章：\n\n{intro_text}'
        )
        
        # 末尾に対応表を追加
        content += outro_text
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✓ {filename} を更新しました')
```

**ステップ3**: 更新後の章ごとのファイルから統合マークダウンを作成

```bash
cat quickstart.md preface.md chapter1_final.md chapter2_final.md \
    chapter3_final.md chapter4_final.md chapter5_final.md \
    chapter6_final.md chapter7_final.md chapter8_final.md \
    chapter9_final.md chapter10_final.md chapter11_final.md \
    chapter12_final.md afterword.md appendix_b_final.md \
    appendix_c_final.md > complete_manuscript_v18.md
```

### 結果

v18は、v13の変更内容を100%反映した完成版となりました。

---

## 問題2: Pandocで大きなファイルを変換すると一部の見出しが認識されない

### 発生日時
2025年12月4日

### 問題の詳細

**症状**:
- v18のマークダウンファイル（8,178行）を単一ファイルとしてPandocで変換すると、17個のHeading 1のうち7個しか認識されない
- 第5章以降の見出しがほとんど欠落

**原因**:
- Pandocには、大きなファイルを変換する際の制限がある
- 約1800行以降の見出しが正しく認識されない場合がある

### 試行した解決策

**試行1**: ファイルを2つに分割して変換

```bash
# 第9章の前（3820行目）で分割
head -3819 complete_manuscript_v18.md > v18_part1.md
tail -n +3820 complete_manuscript_v18.md > v18_part2.md

# 各パートを変換
pandoc v18_part1.md -o v18_part1.docx --reference-doc=v10.docx --toc --toc-depth=2
pandoc v18_part2.md -o v18_part2.docx --reference-doc=v10.docx

# python-docxで結合
python3.11 merge_v18_parts.py
```

**結果**: 第7〜9章が欠落（失敗）

**試行2**: ファイルを4つのグループに分割して変換

```bash
# 4つのグループに分割
# Group1: クイックスタート + はじめに + 第1-4章
# Group2: 第5-9章
# Group3: 第10-12章 + おわりに
# Group4: 付録B + 付録C

# 各グループを変換
for i in 1 2 3 4; do
    pandoc v18_group${i}.md -o v18_group${i}.docx --reference-doc=v10.docx
done

# python-docxで結合
python3.11 merge_v18_groups.py
```

**結果**: Group2で第7〜9章が欠落（失敗）

**試行3**: 章ごとに個別変換してから結合（最終的な解決策）

```bash
# 各章を個別に変換
for i in {0..16}; do
    pandoc chapter_${i}.md -o chapter_${i}.docx --reference-doc=v10.docx
done

# python-docxで結合
python3.11 merge_word_files.py
```

**結果**: すべての章が正しく変換された（成功）

### 解決策

**最終的な解決策**: 章ごとに個別変換してから結合

1. 各章のマークダウンファイルを個別にPandocでWord変換
2. 17個のWordファイルをpython-docxで結合

**メリット**:
- Pandocの制限を回避できる
- 各章が独立して変換されるため、エラーが発生しにくい
- 特定の章のみを再変換することが容易

**デメリット**:
- 変換ファイル数が多くなる（17個）
- 結合処理が必要

---

## 問題3: 「第3部：実践編」がHeading 1として認識される

### 発生日時
2025年12月4日

### 問題の詳細

**症状**:
- v18_finalのWord文書に18個のHeading 1が存在（期待値: 17個）
- 「第3部：実践編 - ベトナム・タイ周遊記」が独立したHeading 1として認識される

**原因**:
- chapter6_final.mdの冒頭に「# 第3部：実践編 - ベトナム・タイ周遊記」が存在
- これはHeading 2であるべきだが、Heading 1として記述されていた

### 解決策

**ステップ1**: chapter6_final.mdの見出しレベルを修正

```bash
sed -i 's/^# 第3部：実践編/## 第3部：実践編/' chapter6_final.md
```

**ステップ2**: chapter_07.docxを再変換

```bash
rm -f chapter_07.docx
pandoc chapter6_final.md -o chapter_07.docx --reference-doc=complete_manuscript_v10.docx
```

**ステップ3**: v18_finalを再作成

```bash
python3.11 merge_word_files.py
```

### 結果

v18_finalのHeading 1が17個になり、期待通りの構造になりました。

---

## 問題4: Pandocが「**本章の使い方**：」を誤認識

### 発生日時
2025年12月4日

### 問題の詳細

**症状**:
- 第6〜9章の冒頭に追加した「**本章の使い方**：本章では...」がPandocに誤認識される
- YAMLメタデータとして処理され、その後の見出しが正しく変換されない

**原因**:
- Pandocは、行頭の`**text**:`をYAMLメタデータの可能性があると判断
- 特に、見出しの直後にこの形式があると誤認識しやすい

### 試行した解決策

**試行1**: 太字と本文を別の段落に分ける

```markdown
# 第6章：旅行前の準備に使える「6つの型」

**本章の使い方**

本章では、実際の旅行体験を通じて「なぜそのプロンプトを使ったのか」「どう改善したのか」を学べます。
```

**結果**: 一部改善されたが、完全には解決しなかった

**試行2**: 見出しの直後の重複タイトル行を削除

chapter6_final.mdの見出しの直後に「旅行前の準備に使える「6つの型」」という重複行が存在していたため、これを削除：

```bash
sed -i '/^# 第6章：/,/^---$/{
    /^旅行前の準備に使える「6つの型」$/d
}' chapter6_final.md
```

**結果**: 問題が解決し、すべての章が正しく変換された

### 解決策

**最終的な解決策**: 見出しの直後の重複タイトル行を削除

1. 見出しの直後に同じタイトルが通常のテキストとして存在しないことを確認
2. 「**本章の使い方**」と本文を別の段落に分ける
3. 章ごとに個別変換することで、Pandocの誤認識を最小化

---

## 問題5: python-docxでの結合時にフォーマットが崩れる

### 発生日時
2025年12月4日（初期の試行時）

### 問題の詳細

**症状**:
- python-docxで複数のWord文書を結合すると、フォーマットが崩れる場合がある
- 特に、異なる参照用Word文書を使用した場合に発生

**原因**:
- 各章のWord文書が異なるスタイル定義を持っている
- 結合時にスタイルの競合が発生

### 解決策

**すべての章で同じ参照用Word文書を使用**

```bash
# すべての章で同じ参照用Word文書を使用
pandoc chapter6_final.md -o chapter_07.docx \
    --reference-doc=complete_manuscript_v10.docx
```

**メリット**:
- スタイルの一貫性が保たれる
- 結合後のフォーマットが崩れない

---

## 学んだ教訓

### 1. 大きなファイルは章ごとに分割して変換

Pandocには大きなファイルを変換する際の制限があるため、章ごとに個別変換してから結合する方が確実です。

### 2. 見出しレベルの一貫性を保つ

マークダウンファイルの見出しレベルが正しいことを確認してから変換することが重要です。

### 3. 参照用Word文書を統一

すべての章で同じ参照用Word文書を使用することで、スタイルの一貫性を保つことができます。

### 4. 検証スクリプトを活用

変換後のWord文書の見出し構造を確認するスクリプトを作成し、問題を早期に発見することが重要です。

### 5. 章ごとのファイルを最新の状態に保つ

統合マークダウンファイルだけでなく、章ごとのファイルも最新の状態に保つことで、今後の修正が容易になります。

---

## まとめ

今回の試行錯誤を通じて、以下のプロセスが最も確実であることが判明しました：

1. **章ごとのファイルを最新の状態に保つ**
2. **各章を個別にPandocでWord変換**
3. **python-docxで17個のWordファイルを結合**
4. **検証スクリプトで見出し構造を確認**
5. **Wordで目次を更新し、ページ番号を設定**

このプロセスにより、Amazon KDP用のWord文書を確実に作成できます。

## 参考資料

- [Pandoc User's Guide](https://pandoc.org/MANUAL.html)
- [python-docx Documentation](https://python-docx.readthedocs.io/)
- [Amazon KDP ヘルプ](https://kdp.amazon.co.jp/ja_JP/help)
