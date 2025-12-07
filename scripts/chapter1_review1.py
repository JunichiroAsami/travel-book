import os
from openai import OpenAI

client = OpenAI()

# 第1章ドラフトv2を読み込む
with open("/home/ubuntu/ai_travel_book_project/drafts/chapter1_draft_v2.md", "r", encoding="utf-8") as f:
    chapter_content = f.read()

# レビュープロンプト
review_prompt = f"""あなたは経験豊富な編集者です。以下の第1章の原稿をレビューし、改善点を指摘してください。

【レビュー観点】
1. 構成と流れ：章全体の構成は論理的か、読者を引き込む流れになっているか
2. 表現と文体：文章は読みやすく、説得力があるか
3. 具体性：エピソードや例示は具体的で、読者がイメージしやすいか
4. 一貫性：「AIは相棒である」というメッセージが一貫して伝わるか
5. 誤字脱字・文法：明らかな誤りはないか

【原稿】
{chapter_content}

【出力形式】
以下の形式で、具体的かつ建設的なフィードバックを提供してください：

## 総評
（全体的な印象と評価）

## 具体的な改善点
### 1. 構成と流れ
（指摘事項）

### 2. 表現と文体
（指摘事項）

### 3. 具体性
（指摘事項）

### 4. 一貫性
（指摘事項）

### 5. 誤字脱字・文法
（指摘事項）

## 優れている点
（良かった点を3つ以上）
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
with open("/home/ubuntu/ai_travel_book_project/reviews/chapter1_editor_review_round1.md", "w", encoding="utf-8") as f:
    f.write("# 第1章 編集者レビュー（第1回）\n\n")
    f.write(f"**レビュー日**: 2025-11-26\n\n")
    f.write(f"**対象**: chapter1_draft_v2.md\n\n")
    f.write("---\n\n")
    f.write(review_result)

print("レビューが完了しました。")
print(f"\n{review_result}")
