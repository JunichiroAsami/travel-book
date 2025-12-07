#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化
client = OpenAI()

# 第12章の原稿を読み込む
with open('/home/ubuntu/ai_travel_book_project/final/chapter12_final.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# 7観点レビュープロンプト
review_prompt = f"""
以下は、AI旅行記の第12章「あなたの旅を変える第一歩」の最終原稿です。
この章は、本書の最終章であり、読者に向けた「次の一歩」を提案する重要な章です。

あなたは経験豊富な編集者として、以下の7つの観点から原稿を評価してください。

【評価観点】
1. トレーサビリティ（実例の活用と引用の正確性）
2. 実用性（読者が実際に行動に移せるか）
3. 一貫性（他章との整合性、全体の流れ）
4. 読みやすさ（文章の明快さ、リズム）
5. 情報の正確性（事実関係の正確さ）
6. 読者への訴求力（感動的か、心に響くか）
7. 完成度（最終章として適切か）

【出力形式】
各観点について、以下の形式で評価してください：
- 評価（5段階：1=不十分、2=要改善、3=普通、4=良好、5=優秀）
- 理由（具体的に）
- 改善提案（あれば）

最後に、総合評価（5段階）と総評を記載してください。

---

【第12章の原稿】

{chapter_content}
"""

# ChatGPT APIを呼び出して7観点レビューを実行
print("7観点レビューを実行中...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。原稿を7つの観点から客観的かつ建設的にレビューしてください。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

# レビュー結果を取得
review_result = response.choices[0].message.content

# レビュー結果をファイルに保存
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter12_7aspect_review.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# 第12章 7観点レビュー\n\n")
    f.write(f"**実行日時**: 2025-11-26\n\n")
    f.write("---\n\n")
    f.write(review_result)

print(f"\nレビュー結果を {output_path} に保存しました。")
print("\n" + "="*50)
print(review_result)
