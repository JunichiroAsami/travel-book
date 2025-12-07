#!/usr/bin/env python3.11
"""
第7章編集者レビュー（第1回）スクリプト

このスクリプトは、ChatGPT API（gpt-4.1-mini）を使用して、
第7章ドラフトを編集者の視点でレビューします。
"""

import os
from openai import OpenAI

# OpenAI APIクライアントの初期化（環境変数から自動設定）
client = OpenAI()

# 第7章ドラフトを読み込み
with open('/home/ubuntu/ai_travel_book_project/drafts/chapter7_for_review.md', 'r', encoding='utf-8') as f:
    chapter7_draft = f.read()

# 編集者レビュー用のプロンプト
editor_prompt = f"""
あなたは、旅行ガイドブックの編集者です。以下の第7章ドラフトをレビューしてください。

# レビュー観点

1. **構成と論理性**: 章の構成が明確で、論理的な流れになっているか
2. **読者目線**: 読者が理解しやすく、実践しやすい内容になっているか
3. **具体性**: 抽象的な説明ではなく、具体的な例が豊富に盛り込まれているか
4. **プロンプトの実用性**: プロンプト例が実際に使えるものになっているか
5. **トレーサビリティ**: 実際のログに基づいているか、ログIDとファイル名が記載されているか
6. **文体とトーン**: 親しみやすく、読みやすい文体になっているか

# レビュー形式

以下の形式でレビューを提供してください：

## 総合評価

（5段階評価：1〜5）

## 強み

（3つ以上）

## 改善提案

（優先度高、優先度中、優先度低に分けて、具体的な改善提案を提供）

## 詳細コメント

（各シーンごとに、具体的なコメントを提供）

---

# 第7章ドラフト

{chapter7_draft}
"""

# ChatGPT APIでレビューを実行
print("ChatGPT API編集者レビュー（第1回）を開始します...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは、旅行ガイドブックの編集者です。ドラフトを読者目線でレビューし、具体的な改善提案を提供します。"},
        {"role": "user", "content": editor_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

# レビュー結果を取得
review_result = response.choices[0].message.content

# レビュー結果を保存
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter7_editor_review_round1.md', 'w', encoding='utf-8') as f:
    f.write("# 第7章編集者レビュー（第1回）\n\n")
    f.write(f"**レビュー日**: 2025-11-26\n\n")
    f.write(f"**レビュー対象**: 第7章ドラフトv1\n\n")
    f.write("---\n\n")
    f.write(review_result)

print("ChatGPT API編集者レビュー（第1回）が完了しました。")
print("レビュー結果: /home/ubuntu/ai_travel_book_project/reviews/chapter7_editor_review_round1.md")
