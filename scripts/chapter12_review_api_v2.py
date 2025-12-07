#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化
client = OpenAI()

# 第12章の原稿を読み込む
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter12_review_v2.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# レビュープロンプト
review_prompt = f"""
以下は、AI旅行記の第12章「あなたの旅を変える第一歩」の原稿です。
この章は、本書の最終章であり、読者に向けた「次の一歩」を提案する重要な章です。

あなたは経験豊富な編集者として、以下の観点から原稿をレビューし、改善提案を行ってください。

【レビュー観点】
1. 全体の構成と流れ
   - 最終章として適切な構成になっているか
   - 各節のつながりが自然か
   - 読者へのメッセージが明確か

2. 内容の質
   - 実例（LOG）の引用が効果的か
   - 3つのアクションが具体的で実践的か
   - 「おわりに」が読者の心に響くか

3. 表現と文体
   - 冗長な表現はないか
   - 文章のリズムは良いか
   - 専門用語の説明は十分か

4. 読者への訴求力
   - 読者が「やってみよう」と思えるか
   - 感動的なエンディングになっているか

【出力形式】
1. 総合評価（5段階）
2. 良い点（3つ）
3. 改善提案（具体的に5つ）
4. 推定文字数と目標文字数（4,000～5,000文字）との比較

---

【第12章の原稿】

{chapter_content}
"""

# ChatGPT APIを呼び出してレビューを実行
print("ChatGPT API編集者レビュー（第2回）を実行中...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。原稿を客観的かつ建設的にレビューしてください。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7,
    max_tokens=3000
)

# レビュー結果を取得
review_result = response.choices[0].message.content

# レビュー結果をファイルに保存
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter12_api_review_v2.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# 第12章 ChatGPT API編集者レビュー（第2回）\n\n")
    f.write(f"**実行日時**: 2025-11-26\n\n")
    f.write("---\n\n")
    f.write(review_result)

print(f"\nレビュー結果を {output_path} に保存しました。")
print("\n" + "="*50)
print(review_result)
