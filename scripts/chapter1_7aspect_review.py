import os
from openai import OpenAI

client = OpenAI()

# 第1章ドラフトv4を読み込む
with open("/home/ubuntu/ai_travel_book_project/drafts/chapter1_draft_v4.md", "r", encoding="utf-8") as f:
    chapter_content = f.read()

# 7観点レビュープロンプト
review_prompt = f"""あなたは経験豊富な編集者です。以下の第1章の原稿を、7つの観点から総合的にレビューし、各観点で5段階評価（1: 不十分、2: やや不十分、3: 普通、4: 良好、5: 優秀）を行ってください。

【原稿】
{chapter_content}

【レビュー観点】
1. 内容の正確性：情報は正確で、誤解を招く表現はないか
2. 論理構成：章全体の論理展開は明確で、読者が理解しやすいか
3. 文章品質：文章は読みやすく、適切な表現が使われているか
4. 読者への訴求力：読者の興味を引き、共感を呼ぶ内容になっているか
5. 独自性・新規性：他の類書にはない独自の視点や価値があるか
6. 実用性：読者が実際に活用できる情報が含まれているか
7. 全体的完成度：出版物として十分な品質に達しているか

【出力形式】
## 7観点評価

### 1. 内容の正確性
**評価**: X/5
**コメント**: （具体的な評価理由）

### 2. 論理構成
**評価**: X/5
**コメント**: （具体的な評価理由）

### 3. 文章品質
**評価**: X/5
**コメント**: （具体的な評価理由）

### 4. 読者への訴求力
**評価**: X/5
**コメント**: （具体的な評価理由）

### 5. 独自性・新規性
**評価**: X/5
**コメント**: （具体的な評価理由）

### 6. 実用性
**評価**: X/5
**コメント**: （具体的な評価理由）

### 7. 全体的完成度
**評価**: X/5
**コメント**: （具体的な評価理由）

## 総合評価
**平均スコア**: X.X/5
**総評**: （全体的な評価と最終判定）

## 改善提案
（さらなる改善のための具体的な提案があれば記載）
"""

# APIを呼び出してレビューを取得
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。原稿を7つの観点から総合的にレビューし、具体的で建設的なフィードバックを提供します。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7
)

review_result = response.choices[0].message.content

# レビュー結果を保存
with open("/home/ubuntu/ai_travel_book_project/reviews/chapter1_7aspect_review.md", "w", encoding="utf-8") as f:
    f.write("# 第1章 7観点レビュー\n\n")
    f.write(f"**レビュー日**: 2025-11-26\n\n")
    f.write(f"**対象**: chapter1_draft_v4.md\n\n")
    f.write("---\n\n")
    f.write(review_result)

print("7観点レビューが完了しました。")
print(f"\n{review_result}")
