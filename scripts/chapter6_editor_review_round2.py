#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化
client = OpenAI()

# 第6章ドラフト（修正後）を読み込む
with open('/home/ubuntu/ai_travel_book_project/drafts/chapter6_for_review_round2.md', 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# 第1回レビュー結果を読み込む
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter6_editor_review_round1.md', 'r', encoding='utf-8') as f:
    first_review = f.read()

# 編集者レビュー用のプロンプト
review_prompt = f"""
あなたは経験豊富な書籍編集者です。以下の第6章のドラフト（第1回レビュー後の修正版）をレビューし、改善提案を行ってください。

# 第1回レビュー結果

{first_review}

# レビュー対象（修正後）

{chapter_content}

# レビュー観点

1. **第1回レビューの改善提案への対応状況**: 第1回レビューの改善提案がどの程度反映されているか
2. **構成・論理性**: 章全体の構成は論理的か、各節の流れは自然か
3. **文章の質**: 文章は読みやすいか、冗長な表現はないか
4. **読者体験**: 読者が「自分も使ってみたい」と思えるか
5. **完成度**: 誤字脱字、表記揺れはないか

# レビュー形式

以下の形式でレビュー結果を出力してください：

## 総合評価

[1-5点で評価し、理由を記載]

## 第1回レビューからの改善点

[第1回レビューの改善提案がどの程度反映されたかを評価]

## 強み

[この章の強みを3つ挙げる]

## 改善提案

### 優先度高

[最も重要な改善提案を挙げる（なければ「なし」）]

### 優先度中

[重要度が中程度の改善提案を挙げる（なければ「なし」）]

### 優先度低

[あれば良い改善提案を挙げる（なければ「なし」）]

## 具体的な修正案

[具体的な修正案があれば記載]
"""

# ChatGPT APIを使用してレビューを実行
print("ChatGPT API編集者レビュー（第2回）を実行中...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な書籍編集者です。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

# レビュー結果を取得
review_result = response.choices[0].message.content

# レビュー結果を保存
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter6_editor_review_round2.md'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# 第6章 編集者レビュー（第2回）\n\n")
    f.write(f"**レビュー日**: 2025-11-26\n\n")
    f.write("---\n\n")
    f.write(review_result)

print(f"レビュー結果を保存しました: {output_path}")
