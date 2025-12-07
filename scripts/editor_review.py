#!/usr/bin/env python3
"""
ChatGPT API編集者レビュースクリプト
"""

import os
from openai import OpenAI

def main():
    # OpenAI APIクライアントの初期化
    client = OpenAI()
    
    # プロンプトファイルの読み込み
    with open('/home/ubuntu/ai_travel_book_project/prompts/chapter5_editor_review_prompt.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    
    # 第5章ドラフトv3の読み込み
    with open('/home/ubuntu/ai_travel_book_project/reviews/chapter5_for_review.md', 'r', encoding='utf-8') as f:
        chapter5_draft = f.read()
    
    # プロンプトの作成
    full_prompt = f"{prompt_template}\n\n## 原稿\n\n{chapter5_draft}"
    
    print("ChatGPT API編集者レビューを開始します...")
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
    output_path = '/home/ubuntu/ai_travel_book_project/reviews/chapter5_editor_review_round1.md'
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
