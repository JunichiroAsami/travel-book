#!/usr/bin/env python3
"""
第12章のChatGPT API編集者レビュー（第1回）
"""

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化
client = OpenAI()

# レビュー対象ファイルの読み込み
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter12_review_v1.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# レビュープロンプトの作成
review_prompt = f"""
あなたは経験豊かな編集者です。以下の原稿（第12章：あなたの旅を変える第一歩）を、出版に向けてレビューしてください。

# レビュー観点
1. 文章の読みやすさ（冗長な表現、わかりにくい表現）
2. 構成の論理性（章の流れ、節の配置）
3. 読者への訴求力（感動を与える表現、行動を促す表現）
4. 専門用語の説明の適切性
5. 全体のバランス（各節の文字数、内容の濃淡）

# 原稿
{chapter_content}

# レビュー結果の形式
以下の形式で回答してください：

## 総合評価
（5段階評価と総評）

## 良い点
（箇条書きで3〜5点）

## 改善提案
（箇条書きで5〜7点、具体的な修正案を含む）

## 文字数について
（目標文字数: 4,000～5,000文字に対する評価）
"""

# APIリクエストの実行
print("ChatGPT API編集者レビュー（第1回）を実行中...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊かな編集者です。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

# レビュー結果の取得
review_result = response.choices[0].message.content

# レビュー結果の保存
output_file = '/home/ubuntu/ai_travel_book_project/reviews/chapter12_api_review_v1.md'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# 第12章 ChatGPT API編集者レビュー（第1回）\n\n")
    f.write(review_result)

print(f"レビュー結果を {output_file} に保存しました。")
print("\n" + "="*80)
print(review_result)
print("="*80)
