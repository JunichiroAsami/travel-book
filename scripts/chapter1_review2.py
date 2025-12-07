import os
from openai import OpenAI

client = OpenAI()

# 第1章ドラフトv3を読み込む
with open("/home/ubuntu/ai_travel_book_project/drafts/chapter1_draft_v3.md", "r", encoding="utf-8") as f:
    chapter_content = f.read()

# レビュープロンプト
review_prompt = f"""あなたは経験豊富な編集者です。以下の第1章の原稿（修正版v3）をレビューし、改善点を指摘してください。

この原稿は、第1回レビューの指摘を受けて修正されたものです。特に以下の点に注目してレビューしてください：
1. 構成とメリハリ：3つのエピソードに小見出しを追加した効果は十分か
2. 読みやすさ：小見出しの追加により、視覚的な読みやすさは向上したか
3. リズムと緩急：文章のリズムは改善されたか
4. 全体の完成度：出版可能なレベルに達しているか

【原稿】
{chapter_content}

【出力形式】
以下の形式で、具体的かつ建設的なフィードバックを提供してください：

## 総評
（全体的な印象と評価、第1回レビューからの改善度）

## 具体的な改善点
### 1. 構成とメリハリ
（指摘事項）

### 2. 読みやすさ
（指摘事項）

### 3. リズムと緩急
（指摘事項）

### 4. その他の気になる点
（指摘事項）

## 優れている点
（良かった点を3つ以上）

## 最終判定
（出版可能レベルに達しているか、さらなる修正が必要か）
"""

# APIを呼び出してレビューを取得
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。原稿を丁寧にレビューし、具体的で建設的なフィードバックを提供します。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7
)

review_result = response.choices[0].message.content

# レビュー結果を保存
with open("/home/ubuntu/ai_travel_book_project/reviews/chapter1_editor_review_round2.md", "w", encoding="utf-8") as f:
    f.write("# 第1章 編集者レビュー（第2回）\n\n")
    f.write(f"**レビュー日**: 2025-11-26\n\n")
    f.write(f"**対象**: chapter1_draft_v3.md\n\n")
    f.write("---\n\n")
    f.write(review_result)

print("レビューが完了しました。")
print(f"\n{review_result}")
