#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第10章 ChatGPT API編集者レビュー（第2回）
"""

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化
client = OpenAI()

# 第10章の原稿を読み込み
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter10_review_v2.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# レビュー依頼のプロンプト
review_prompt = f"""
以下は、AI旅行に関する書籍の第10章「AI旅行の光と影」の原稿です。

この原稿は、第1回のレビューフィードバックに基づいて修正されたものです。
第2回のレビューとして、以下の観点から評価し、改善提案を行ってください。

【レビュー観点】
1. 第1回レビューの指摘事項が適切に反映されているか
2. 専門用語の説明の充実度（ハルシネーション、デジタルデバイドなど）
3. 文章の読みやすさとリズム（長文の簡潔化、冗長性の削減）
4. LOG引用の効果的な使用（要点抽出、注釈の追加）
5. 「影」のリスクの具体的対策例の充実度
6. まとめの簡潔性と効果性
7. 全体のバランスと完成度

【評価形式】
1. 総合評価（5段階）
2. 各観点の評価と具体的な改善提案
3. 優れている点
4. 残存する改善が必要な点
5. 文字数の適切性（目標: 7,000～9,000文字）

---

【第10章の原稿】

{chapter_content}
"""

# ChatGPT APIを使用してレビューを実行
print("ChatGPT API編集者レビュー（第2回）を実行中...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。AI旅行に関する書籍の原稿をレビューし、建設的なフィードバックを提供してください。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

# レビュー結果を取得
review_result = response.choices[0].message.content

# レビュー結果をファイルに保存
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter10_api_review_v2.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# 第10章 ChatGPT API編集者レビュー（第2回）\n\n")
    f.write(review_result)

print(f"レビュー結果を {output_path} に保存しました。")
print("\n" + "="*80)
print(review_result)
print("="*80)
