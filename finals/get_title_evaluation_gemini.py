#!/usr/bin/env python3
"""Gemini 2.5 Flashにタイトル案の評価を依頼するスクリプト"""

import os
from openai import OpenAI

# OpenAI互換APIを使用してGeminiにアクセス
client = OpenAI()

# プロンプトを読み込む
with open('/home/ubuntu/ai_travel_book_project/finals/title_evaluation_prompt.md', 'r', encoding='utf-8') as f:
    prompt_template = f.read()

# タイトルを改善案1に変更
prompt = prompt_template.replace(
    "ChatGPTと旅するベトナム・タイ：プロンプトで言葉の壁を越える",
    "ChatGPTと旅するベトナム・タイ：AI活用で言葉の壁を越える実践ガイド"
)

print("Gemini 2.5 Flashにタイトル評価を依頼中...")
print("=" * 80)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": "あなたは20年以上の経験を持つベテラン出版編集者です。特に旅行書とビジネス書の分野で数多くのベストセラーを手がけてきました。タイトル選定において、読者心理、SEO、マーケティング戦略を総合的に判断することに長けています。率直かつ建設的なフィードバックを提供してください。"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7,
    max_tokens=3000
)

result = response.choices[0].message.content

print(result)
print("=" * 80)

# 結果を保存
with open('/home/ubuntu/ai_travel_book_project/finals/gemini_title_evaluation.md', 'w', encoding='utf-8') as f:
    f.write("# Gemini 2.5 Flash によるタイトル評価\n\n")
    f.write("## 評価対象タイトル\n\n")
    f.write("**タイトル**: ChatGPTと旅するベトナム・タイ：AI活用で言葉の壁を越える実践ガイド\n\n")
    f.write("---\n\n")
    f.write(result)

print("\n結果を保存しました: gemini_title_evaluation.md")
