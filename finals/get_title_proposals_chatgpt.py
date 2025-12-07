#!/usr/bin/env python3
"""ChatGPT GPT-4.1-miniにタイトル案を提案してもらうスクリプト"""

import os
from openai import OpenAI

# OpenAI互換APIを使用してChatGPTにアクセス
client = OpenAI()

# プロンプトを読み込む
with open('/home/ubuntu/ai_travel_book_project/finals/title_proposal_prompt.md', 'r', encoding='utf-8') as f:
    prompt = f.read()

print("ChatGPT GPT-4.1-miniにタイトル案を依頼中...")
print("=" * 80)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "あなたは経験豊富な出版編集者であり、マーケティングの専門家です。書籍のタイトル提案において、読者の心を掴み、売上を最大化するタイトルを考案することに長けています。"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.8,
    max_tokens=4000
)

result = response.choices[0].message.content

print(result)
print("=" * 80)

# 結果を保存
with open('/home/ubuntu/ai_travel_book_project/finals/chatgpt_title_proposals.md', 'w', encoding='utf-8') as f:
    f.write("# ChatGPT GPT-4.1-mini によるタイトル提案\n\n")
    f.write(result)

print("\n結果を保存しました: chatgpt_title_proposals.md")
