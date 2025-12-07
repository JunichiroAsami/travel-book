#!/usr/bin/env python3.11
"""
第8章編集者レビュー（第2回）スクリプト
"""

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化（環境変数から自動設定）
client = OpenAI()

# 第8章ドラフト（修正後）を読み込む
with open('/home/ubuntu/ai_travel_book_project/drafts/chapter8_for_review_round2.md', 'r', encoding='utf-8') as f:
    chapter8_draft = f.read()

# 第1回レビュー結果を読み込む
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter8_editor_review_round1.md', 'r', encoding='utf-8') as f:
    review_round1 = f.read()

# 編集者レビュープロンプト
editor_prompt = f"""あなたは経験豊富な書籍編集者です。以下の第8章「トラブル対応の『緊急プロンプト集』」のドラフト（修正後）をレビューしてください。

【第1回レビュー結果】
{review_round1}

【第1回レビューからの主な修正内容】
1. 読者ターゲットの明確化：章の導入部に「**AIを初めて使う方でもすぐに使える形**」を追加
2. 用語・表記の統一：「保険補償範囲」→「保険適用範囲」に統一

【レビュー観点】
1. 第1回レビューの改善提案に対応できているか
2. 構成・論理性：章の構成が明確で、読者が理解しやすいか
3. 読者体験：読者が実際に使える形で提供されているか
4. 文体・トーン：親しみやすく、読みやすい文体か
5. 完成度：誤字脱字、表記の統一、トレーサビリティの確保

【レビュー形式】
- 総合評価（5段階）
- 第1回レビューからの改善点
- 強み（3つ以上）
- 新たな改善提案（優先度高・中・低に分けて、具体的に）

---

【第8章ドラフト（修正後）】

{chapter8_draft}
"""

# ChatGPT APIでレビューを実行
print("ChatGPT API編集者レビュー（第2回）を実行中...")
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
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter8_editor_review_round2.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(f"# 第8章編集者レビュー（第2回）\n\n")
    f.write(f"**実行日時**: 2025-11-26\n\n")
    f.write(f"---\n\n")
    f.write(review_result)

print(f"レビュー結果を {output_path} に保存しました。")
