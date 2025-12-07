import os
from openai import OpenAI

client = OpenAI()

# 第2章ドラフトv4を読み込む
with open('/home/ubuntu/ai_travel_book_project/drafts/chapter2_draft_v4.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# 7観点レビュー用プロンプト
review_prompt = f"""あなたは経験豊富な編集者です。以下の第2章の最終稿を、7つの観点から詳細にレビューしてください。

【第2章の最終稿】
{chapter_content}

【レビューの7つの観点】
1. 内容の正確性（5点満点）：事実関係や論理に誤りがないか
2. 論理構成（5点満点）：論理的で分かりやすい構成になっているか
3. 文章品質（5点満点）：文章が洗練され、読みやすいか
4. 読者への訴求力（5点満点）：読者の心を掴み、読み進めたくなるか
5. 独自性・新規性（5点満点）：他の書籍にはない独自の価値があるか
6. 実用性（5点満点）：読者が実際に活用できる内容か
7. 全体的完成度（5点満点）：出版物として完成度が高いか

【レビュー形式】
各観点について、以下の形式で評価してください：
- 観点名：評価点数（5点満点）
- 評価理由（100文字程度）

最後に、総合評価（35点満点中の合計点）と総評（200文字程度）を記載してください。
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7
)

review_result = response.choices[0].message.content

# レビュー結果を保存
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter2_7aspect_review.md', 'w', encoding='utf-8') as f:
    f.write("# 第2章 7観点レビュー\n\n")
    f.write(f"**レビュー日時**: 2025-11-26\n\n")
    f.write("---\n\n")
    f.write(review_result)

print("7観点レビューが完了しました。")
print(f"\nレビュー結果:\n{review_result}")
