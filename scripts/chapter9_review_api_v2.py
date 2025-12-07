#!/usr/bin/env python3
"""
第9章のChatGPT API編集者レビュースクリプト（第2回）
"""

import os
from openai import OpenAI

# OpenAIクライアントの初期化
client = OpenAI()

# レビュー対象の原稿を読み込む
with open('/home/ubuntu/ai_travel_book_project/reviews/chapter9_review_v2.md', 'r', encoding='utf-8') as f:
    manuscript = f.read()

# レビュープロンプト
review_prompt = f"""
あなたは経験豊富な編集者です。以下の原稿は、「AIと旅する」というテーマの書籍の第9章「旅行後の振り返りに使える『分析プロンプト集』」の改訂版です。

前回のレビューで指摘された以下の点について改善が行われています：
1. 導入部の強化（具体的メリットの数値化）
2. 実例ログの補足説明
3. プロンプトテンプレートのフォーマット統一
4. 専門用語の注釈強化
5. 読者アクションの明示
6. 動画分析のプロンプト具体化
7. まとめの更なる具体化

この改訂版を、以下の観点から再度レビューし、さらなる改善提案を行ってください。

【レビュー観点】
1. **前回指摘事項の改善度**: 前回の指摘が適切に反映されているか？
2. **全体の完成度**: 章として完成度が高く、出版に値する品質か？
3. **読者への訴求力**: 読者が「すぐに試したい」と思える内容になっているか？
4. **細部の洗練度**: 文章表現、用語の統一、誤字脱字などの細部が洗練されているか？
5. **バランス**: 各セクションの分量や深さのバランスは適切か？

【レビュー結果の形式】
- **総合評価**: 5段階評価（1: 要大幅修正、2: 要修正、3: 普通、4: 良好、5: 優秀）
- **改善された点**: 前回からの改善点を3つ以上
- **残存する課題**: まだ改善の余地がある点を3つ以上
- **最終推奨**: このまま確定してよいか、さらなる修正が必要か

---

【原稿】

{manuscript}
"""

# ChatGPT APIでレビューを実行
print("ChatGPT API編集者レビュー（第2回）を実行中...")
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
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter9_review_report_v2.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# 第9章：ChatGPT API編集者レビュー報告書（第2回）\n\n")
    f.write(f"**レビュー日時**: 2025-11-26\n\n")
    f.write(f"**レビュー対象**: chapter9_review_v2.md\n\n")
    f.write("---\n\n")
    f.write(review_result)

print(f"\nレビュー結果を保存しました: {output_path}")
print("\n" + "="*80)
print(review_result)
