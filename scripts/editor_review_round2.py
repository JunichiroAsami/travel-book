#!/usr/bin/env python3
"""
ChatGPT API編集者レビュースクリプト（第2回）
"""

import os
from openai import OpenAI

def main():
    # OpenAI APIクライアントの初期化
    client = OpenAI()
    
    # プロンプトファイルの読み込み
    with open('/home/ubuntu/ai_travel_book_project/prompts/chapter5_editor_review_prompt.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    
    # 第5章ドラフトv3（修正後）の読み込み
    with open('/home/ubuntu/ai_travel_book_project/reviews/chapter5_for_review_round2.md', 'r', encoding='utf-8') as f:
        chapter5_draft = f.read()
    
    # 第1回レビュー結果の読み込み
    with open('/home/ubuntu/ai_travel_book_project/reviews/chapter5_editor_review_round1.md', 'r', encoding='utf-8') as f:
        review_round1 = f.read()
    
    # プロンプトの作成
    full_prompt = f"""{prompt_template}

## 第1回レビュー結果

{review_round1}

## 第1回レビュー後の修正内容

1. 章冒頭の導入強化（読者のよくある悩みを追加）
2. 専門用語の説明を本文中に統合（注釈形式を廃止）
3. 各節のまとめに「AIなしとAIありの違い」を追加
4. 各節のまとめに「読者が実践できる第一歩」を追加

## 原稿（修正後）

{chapter5_draft}

---

第1回レビューの改善提案に対応した修正を行いました。第2回レビューでは、以下の観点で評価してください：
1. 第1回レビューの改善提案が適切に反映されているか
2. 新たに追加した内容（「AIなしとAIありの違い」「読者が実践できる第一歩」）が効果的か
3. 全体的な完成度が向上しているか
4. さらに改善すべき点はあるか
"""
    
    print("ChatGPT API編集者レビュー（第2回）を開始します...")
    print(f"原稿文字数: {len(chapter5_draft)}文字")
    
    # ChatGPT APIを呼び出し
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "あなたは、ビジネス書・紀行文学の編集者です。原稿を編集者の視点でレビューしてください。"},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7,
        max_tokens=4000
    )
    
    # レビュー結果の取得
    review_result = response.choices[0].message.content
    
    # レビュー結果の保存
    output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter5_editor_review_round2.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(review_result)
    
    print(f"\nレビュー結果を保存しました: {output_path}")
    print(f"レビュー文字数: {len(review_result)}文字")
    
    # レビュー結果の一部を表示
    print("\n--- レビュー結果（冒頭部分）---")
    print(review_result[:500])
    print("...")

if __name__ == "__main__":
    main()
