#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from openai import OpenAI

client = OpenAI()

# 第11章の最終版を読み込む
with open('/home/ubuntu/ai_travel_book_project/final/chapter11_final.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# 7観点レビュー用のプロンプト
review_prompt = f"""
あなたは、ビジネス書の編集者です。以下の第11章の最終版を読んで、7つの観点から総合的にレビューしてください。

【第11章の最終版】
{chapter_content}

【レビュー観点】
1. **トレーサビリティ**: 実際のLOG（対話記録）に基づいて記述されているか。LOGの引用は適切か。
2. **実用性**: 読者が実際に使える情報やスキルが提供されているか。
3. **一貫性**: 章全体の論理構成が一貫しているか。矛盾はないか。
4. **読みやすさ**: 文章は読みやすく、理解しやすいか。専門用語の説明は適切か。
5. **情報の正確性**: 記述されている情報は正確か。誤情報はないか。
6. **読者への訴求力**: 読者の関心を引き、行動を促す内容になっているか。
7. **完成度**: 全体として、出版に値する品質に達しているか。

【レビュー結果の出力形式】
- 各観点について、5段階評価（1〜5）と具体的なコメント
- 総合評価（5段階）
- 特に優れている点（3つ）
- 改善の余地がある点（3つ）

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
output_file = '/home/ubuntu/ai_travel_book_project/reviews/chapter11_7aspect_review_result.md'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# 第11章 7観点レビュー結果\n\n")
    f.write(review_result)

print(f"レビュー結果を {output_file} に保存しました。")
print("\n" + "="*80 + "\n")
print(review_result)
