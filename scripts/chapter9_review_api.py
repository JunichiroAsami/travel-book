#!/usr/bin/env python3
"""
第9章のChatGPT API編集者レビュースクリプト
"""

import os
from openai import OpenAI

# OpenAIクライアントの初期化
client = OpenAI()

# レビュー対象の原稿を読み込む
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter9_review_v1.md', 'r', encoding='utf-8') as f:
    manuscript = f.read()

# レビュープロンプト
review_prompt = f"""
あなたは経験豊富な編集者です。以下の原稿は、「AIと旅する」というテーマの書籍の第9章「旅行後の振り返りに使える『分析プロンプト集』」です。

この原稿を、以下の観点から総合的にレビューし、改善提案を行ってください。

【レビュー観点】
1. **構成の論理性**: 章全体の流れは論理的で、読者が理解しやすいか？
2. **具体性と実用性**: プロンプトのテンプレートは具体的で、読者がすぐに使える形になっているか？
3. **トレーサビリティ**: 実際のログへの参照が適切に記載されているか？
4. **文章の明瞭性**: 冗長な表現や不明瞭な箇所はないか？
5. **読者目線**: 読者が「自分も試してみたい」と思えるような書き方になっているか？
6. **専門用語の扱い**: 専門用語に適切な説明が付いているか？
7. **文字数**: 目標文字数（8,000～10,000文字）に対して適切か？

【レビュー結果の形式】
- **総合評価**: 5段階評価（1: 要大幅修正、2: 要修正、3: 普通、4: 良好、5: 優秀）
- **良い点**: 3つ以上
- **改善提案**: 具体的な修正提案を5つ以上
- **文字数評価**: 現在の文字数と、目標に対する評価

---

【原稿】

{manuscript}
"""

# ChatGPT APIでレビューを実行
print("ChatGPT API編集者レビュー（第1回）を実行中...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。原稿を多角的にレビューし、建設的な改善提案を行います。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

review_result = response.choices[0].message.content

# レビュー結果を保存
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter9_review_report_v1.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# 第9章：ChatGPT API編集者レビュー報告書（第1回）\n\n")
    f.write(f"**レビュー日時**: 2025-11-26\n\n")
    f.write(f"**レビュー対象**: chapter9_review_v1.md\n\n")
    f.write("---\n\n")
    f.write(review_result)

print(f"\nレビュー結果を保存しました: {output_path}")
print("\n" + "="*80)
print(review_result)
