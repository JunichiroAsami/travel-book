#!/usr/bin/env python3
"""
第9章の7観点レビュースクリプト
"""

import os
from openai import OpenAI

# OpenAIクライアントの初期化
client = OpenAI()

# レビュー対象の原稿を読み込む
with open('/home/ubuntu/ai_travel_book_project/final/chapter9_final.md', 'r', encoding='utf-8') as f:
    manuscript = f.read()

# 7観点レビュープロンプト
review_prompt = f"""
あなたは経験豊富な編集者です。以下の原稿は、「AIと旅する」というテーマの書籍の第9章「旅行後の振り返りに使える『分析プロンプト集』」の最終版です。

以下の7つの観点から、この原稿を厳密にレビューし、評価と改善提案を行ってください。

【7つのレビュー観点】

1. **トレーサビリティ（追跡可能性）**: 
   - 各プロンプトや実例が、実際のLOGに基づいているか？
   - LOGの引用が正確で、読者が元の対話を追跡できるか？

2. **実用性（Practicality）**: 
   - 読者が実際にプロンプトを使えるか？
   - プロンプトテンプレートは具体的で、再現性があるか？

3. **一貫性（Consistency）**: 
   - 章全体の構成、用語、表記が統一されているか？
   - 他の章（特に第7章、第8章）との整合性はあるか？

4. **読みやすさ（Readability）**: 
   - 文章は明瞭で、専門用語には適切な説明があるか？
   - 段落構成や見出しは読者にとって分かりやすいか？

5. **情報の正確性（Accuracy）**: 
   - 技術的な説明（GPX、JSONL、OCRなど）は正確か？
   - 数値や日付、ファイル名などの具体的な情報に誤りはないか？

6. **読者への訴求力（Appeal）**: 
   - 読者が「自分も試したい」と思える内容になっているか？
   - 具体的なメリットや成果が明示されているか？

7. **完成度（Completeness）**: 
   - 章として必要な要素がすべて揃っているか？
   - 出版に値する品質に達しているか？

【レビュー結果の形式】
各観点について、以下の形式で評価してください。

- **観点名**: 5段階評価（1: 不十分、2: 要改善、3: 普通、4: 良好、5: 優秀）
- **評価理由**: なぜその評価なのか、具体的に説明してください。
- **改善提案**: 評価が4以下の場合、具体的な改善案を提示してください。

最後に、**総合評価**と**最終推奨**を記述してください。

---

【原稿】

{manuscript}
"""

# ChatGPT APIでレビューを実行
print("7観点レビューを実行中...")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。原稿を7つの観点から厳密にレビューし、建設的な改善提案を行います。"},
        {"role": "user", "content": review_prompt}
    ],
    temperature=0.7,
    max_tokens=4000
)

review_result = response.choices[0].message.content

# レビュー結果を保存
output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter9_7aspect_review_report.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# 第9章：7観点レビュー報告書\n\n")
    f.write(f"**レビュー日時**: 2025-11-26\n\n")
    f.write(f"**レビュー対象**: chapter9_final.md\n\n")
    f.write("---\n\n")
    f.write(review_result)

print(f"\nレビュー結果を保存しました: {output_path}")
print("\n" + "="*80)
print(review_result)
