#!/usr/bin/env python3
"""Geminiにディスクレーマーと奥付の文案作成を依頼"""

import os
from openai import OpenAI

# プロンプトを読み込む
with open('/home/ubuntu/ai_travel_book_project/finals/prompt_disclaimer_colophon.md', 'r', encoding='utf-8') as f:
    prompt = f.read()

# Gemini 2.5 Flashを使用
client = OpenAI()

print("Gemini 2.5 Flashにディスクレーマーと奥付の文案作成を依頼中...")
print("=" * 80)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7,
    max_tokens=4000
)

result = response.choices[0].message.content
print(result)
print("=" * 80)

# 結果を保存
with open('/home/ubuntu/ai_travel_book_project/finals/disclaimer_colophon_draft.md', 'w', encoding='utf-8') as f:
    f.write("# ディスクレーマーと奥付の文案（Gemini生成）\n\n")
    f.write(result)

print("\n結果を保存しました: disclaimer_colophon_draft.md")
