#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第10章 ChatGPT API編集者レビュー（第1回）
"""

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化
client = OpenAI()

# 第10章のドラフトを読み込み
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter10_review_v1.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# レビュープロンプト
review_prompt = f"""
あなたは経験豊富な編集者です。以下の第10章「AI旅行の光と影」のドラフトを、プロの視点でレビューしてください。

【レビュー観点】
1. 構成と論理展開の適切性
2. 読者ターゲット（AI旅行に興味がある一般読者）への訴求力
3. 具体例とLOG引用の効果的な使用
4. 文章の読みやすさと表現の適切性
5. 専門用語の説明の充実度
6. 全体のバランス（光と影の分量、3つの原則の説得力）
7. まとめの効果性

【ドラフト内容】
{chapter_content}

【レビュー形式】
1. 総合評価（5段階）
2. 各観点の評価と具体的な改善提案
3. 優れている点
4. 改善が必要な点
5. 文字数の適切性（目標: 7,000～9,000文字）
"""

print("=" * 80)
print("第10章 ChatGPT API編集者レビュー（第1回）")
print("=" * 80)
print()

# APIリクエスト
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富なプロの編集者です。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

# レビュー結果の表示
review_result = response.choices[0].message.content
print(review_result)
print()
print("=" * 80)

# レビュー結果を保存
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter10_api_review_v1.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# 第10章 ChatGPT API編集者レビュー（第1回）\n\n")
    f.write(review_result)

print(f"レビュー結果を保存しました: {output_path}")
