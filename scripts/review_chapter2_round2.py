import os
from openai import OpenAI

client = OpenAI()

# 第2章ドラフトv3を読み込む
with open('/home/ubuntu/ai_travel_book_project/drafts/chapter2_draft_v3.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# レビュー用プロンプト
review_prompt = f"""あなたは経験豊富な編集者です。以下の第2章のドラフト（第1回レビュー後の修正版）を、出版物として適切かどうかレビューしてください。

【第2章のドラフト（修正版）】
{chapter_content}

【レビューの観点】
1. 第1回レビューの指摘事項が適切に反映されているか
2. 読者への訴求力：読者が「読んでみたい」と思う魅力的な内容か
3. 構成の明確さ：論理的で分かりやすい構成になっているか
4. 文章の読みやすさ：リズムが良く、読みやすい文章か
5. 表現の適切さ：過度な表現や不適切な表現がないか

【レビュー形式】
- 総評（200文字程度）
- 良い点（3つ）
- 改善点（あれば3つ、なければ「特になし」）
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
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter2_editor_review_round2.md', 'w', encoding='utf-8') as f:
    f.write("# 第2章 編集者レビュー（第2回）\n\n")
    f.write(f"**レビュー日時**: 2025-11-26\n\n")
    f.write("---\n\n")
    f.write(review_result)

print("第2回レビューが完了しました。")
print(f"\nレビュー結果:\n{review_result}")
