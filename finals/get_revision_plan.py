#!/usr/bin/env python3
"""Geminiに包括的な修正計画を依頼"""

import os
from openai import OpenAI

# OpenAI互換のクライアントを作成（Geminiを使用）
client = OpenAI()

# プロンプトを読み込む
with open('/home/ubuntu/ai_travel_book_project/finals/prompt_revision_plan.md', 'r', encoding='utf-8') as f:
    prompt = f.read()

print("Gemini 2.5 Flashに包括的な修正計画を依頼中...")
print("=" * 80)

# Gemini 2.5 Flashに修正計画を依頼
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7,
    max_tokens=16000
)

# 結果を取得
plan = response.choices[0].message.content

print(plan)
print("=" * 80)

# 結果を保存
with open('/home/ubuntu/ai_travel_book_project/finals/revision_plan_v31.md', 'w', encoding='utf-8') as f:
    f.write(plan)

print("結果を保存しました: revision_plan_v31.md")
