#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第10章 7観点レビュー
"""

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化
client = OpenAI()

# 第10章の原稿を読み込み
with open('/home/ubuntu/ai_travel_book_project/final/chapter10_final.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# 7観点レビューのプロンプト
review_prompt = f"""
以下は、AI旅行に関する書籍の第10章「AI旅行の光と影」の最終原稿です。

この原稿を、以下の7つの観点から厳格にレビューし、評価と改善提案を行ってください。

【7つの観点】
1. **トレーサビリティ（Traceability）**: 実際のLOGとの整合性、引用の正確性
2. **実用性（Practicality）**: 読者が実際に活用できる具体性と実践性
3. **一貫性（Consistency）**: 他の章との整合性、用語・表記の統一性
4. **読みやすさ（Readability）**: 文章の流れ、構成、表現の適切性
5. **情報の正確性（Accuracy）**: 事実関係、専門用語の説明の正確性
6. **読者への訴求力（Appeal）**: 読者の興味を引き、価値を提供できているか
7. **完成度（Completeness）**: 出版に向けた完成度、残存する課題の有無

【評価形式】
- 各観点について、5段階評価（1=不十分、2=要改善、3=普通、4=良好、5=優秀）
- 各観点の具体的な評価コメント
- 総合評価（5段階）
- 優れている点
- 改善が必要な点
- 出版に向けた最終的な推奨事項

---

【第10章の原稿】

{chapter_content}
"""

# ChatGPT APIを使用して7観点レビューを実行
print("7観点レビューを実行中...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。AI旅行に関する書籍の原稿を、7つの観点から厳格にレビューし、出版に向けた最終的な評価を提供してください。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

# レビュー結果を取得
review_result = response.choices[0].message.content

# レビュー結果をファイルに保存
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter10_7aspect_review.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# 第10章 7観点レビュー\n\n")
    f.write(review_result)

print(f"レビュー結果を {output_path} に保存しました。")
print("\n" + "="*80)
print(review_result)
print("="*80)
