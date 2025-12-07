#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from openai import OpenAI

client = OpenAI()

# 第11章のドラフト（修正版）を読み込む
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter11_review_v2.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# ChatGPT API編集者レビュー用のプロンプト
review_prompt = f"""
あなたは、ビジネス書の編集者です。以下の第11章のドラフト（修正版）を読んで、編集者の視点から総合的にレビューしてください。

【第11章のドラフト（修正版）】
{chapter_content}

【レビュー観点】
1. 前回のレビューで指摘した改善提案が反映されているか
2. 文章の読みやすさ（冗長な表現、わかりにくい表現はないか）
3. 論理構成の明確さ（主張と根拠が明確か）
4. 実例の効果的な活用（LOG引用が効果的に使われているか）
5. 専門用語の説明の適切さ
6. 章全体のバランス（各スキルの説明量のバランスは適切か）
7. まとめの充実度（読者が次のアクションを取れるか）
8. 文字数の評価（目標: 7,000〜8,000文字）

【レビュー結果の出力形式】
- 総合評価（5段階）
- 前回からの改善点（3つ）
- 残存課題（3つ）
- 文字数の評価（目標: 7,000〜8,000文字）

よろしくお願いします。
"""

# ChatGPT APIにレビューを依頼
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは、ビジネス書の編集者です。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7
)

# レビュー結果を取得
review_result = response.choices[0].message.content

# レビュー結果を保存
output_file = '/home/ubuntu/ai_travel_book_project/reviews/chapter11_review_api_result_v2.md'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# 第11章 ChatGPT API編集者レビュー（第2回）\n\n")
    f.write(review_result)

print(f"レビュー結果を {output_file} に保存しました。")
print("\n" + "="*80 + "\n")
print(review_result)
