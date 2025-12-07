import os
from openai import OpenAI

client = OpenAI()

# 第2章ドラフトv2を読み込む
with open('/home/ubuntu/ai_travel_book_project/drafts/chapter2_draft_v2.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# レビュー用プロンプト
review_prompt = f"""あなたは経験豊富な編集者です。以下の第2章のドラフトを、出版物として適切かどうかレビューしてください。

【第2章のドラフト】
{chapter_content}

【レビューの観点】
1. 読者への訴求力：読者が「読んでみたい」と思う魅力的な内容か
2. 構成の明確さ：論理的で分かりやすい構成になっているか
3. 文章の読みやすさ：リズムが良く、読みやすい文章か
4. 表現の適切さ：過度な表現や不適切な表現がないか
5. 第1章との連携：第1章からスムーズに繋がっているか

【レビュー形式】
- 総評（200文字程度）
- 良い点（3つ）
- 改善点（3つ）
- 最終判定（出版可能レベル / 要修正 / 大幅な改稿が必要）
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
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter2_editor_review_round1.md', 'w', encoding='utf-8') as f:
    f.write("# 第2章 編集者レビュー（第1回）\n\n")
    f.write(f"**レビュー日時**: 2025-11-26\n\n")
    f.write("---\n\n")
    f.write(review_result)

print("第1回レビューが完了しました。")
print(f"\nレビュー結果:\n{review_result}")
