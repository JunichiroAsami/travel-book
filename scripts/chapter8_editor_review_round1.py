#!/usr/bin/env python3.11
"""
第8章編集者レビュー（第1回）スクリプト
"""

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化（環境変数から自動設定）
client = OpenAI()

# 第8章ドラフトを読み込む
with open('/home/ubuntu/ai_travel_book_project/drafts/chapter8_for_review.md', 'r', encoding='utf-8') as f:
    chapter8_draft = f.read()

# 編集者レビュープロンプト
editor_prompt = f"""あなたは経験豊富な書籍編集者です。以下の第8章「トラブル対応の『緊急プロンプト集』」のドラフトをレビューしてください。

【レビュー観点】
1. 構成・論理性：章の構成が明確で、読者が理解しやすいか
2. 読者体験：読者が実際に使える形で提供されているか
3. 文体・トーン：親しみやすく、読みやすい文体か
4. 完成度：誤字脱字、表記の統一、トレーサビリティの確保
5. 第5章との差別化：第5章（ストーリー重視）と第8章（実践手順重視）の差別化が明確か

【レビュー形式】
- 総合評価（5段階）
- 強み（3つ以上）
- 改善提案（優先度高・中・低に分けて、具体的に）

---

【第8章ドラフト】

{chapter8_draft}
"""

# ChatGPT APIでレビューを実行
print("ChatGPT API編集者レビュー（第1回）を実行中...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な書籍編集者です。"},
        {"role": "user", "content": editor_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

review_result = response.choices[0].message.content

# レビュー結果を保存
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter8_editor_review_round1.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(f"# 第8章編集者レビュー（第1回）\n\n")
    f.write(f"**実行日時**: 2025-11-26\n\n")
    f.write(f"---\n\n")
    f.write(review_result)

print(f"レビュー結果を {output_path} に保存しました。")
