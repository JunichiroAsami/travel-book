#!/usr/bin/env python3
"""
GeminiとChatGPTにシニア編集者としてのレビューを依頼するスクリプト v2
既存のPDF画像を使用
"""

import os
import json
import base64
from openai import OpenAI

# OpenAI クライアントの初期化
client = OpenAI()

print("="*60)
print("シニア編集者レビュー依頼スクリプト v2")
print("="*60)

# 既存のPDF画像を使用（すでに抽出済み）
pdf_image_dir = '/tmp/pdf_images/complete_manuscript_v27_safe'
sample_pages = [1, 5, 10, 20, 35, 40, 100, 150, 200]

# プロンプト
prompt = """あなたは、シニア編集者です。書籍のデザイン及び内容に関して、厳しくレビューしてください。また、改善案があれば指摘してください。

この書籍は「AIツアーコンダクターと歩く ベトナム・タイ周遊記」というタイトルで、AI活用の旅行ガイドブックです。

以下の観点から、厳しくレビューしてください：

1. **デザインの洗練度**: 表紙、目次、本文レイアウト、フォント、余白、ヘッダー・フッター
2. **内容の質**: 情報の正確性、論理的な構成、読みやすさ、専門性
3. **商業出版物としての完成度**: 市販の書籍と比較して、どの程度のレベルか
4. **改善が必要な箇所**: 具体的にどこをどう改善すべきか

**評価基準**:
- ★★★★★ (5.0): 商業出版物として完璧
- ★★★★☆ (4.0): 商業出版物として十分な品質
- ★★★☆☆ (3.0): 改善が必要だが、骨格はしっかりしている
- ★★☆☆☆ (2.0): 大幅な改善が必要
- ★☆☆☆☆ (1.0): 出版には不適切

厳しく、率直に評価してください。"""

# 画像を読み込み
print("\n画像を読み込み中...")
image_contents = []
for page_num in sample_pages:
    img_path = f'{pdf_image_dir}/{page_num:03d}.webp'
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
            image_contents.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/webp;base64,{image_data}"
                }
            })
        print(f"  ✅ ページ{page_num}を読み込み")

print(f"\n合計{len(image_contents)}ページの画像を読み込みました")

# ===== Gemini 2.5 Flash =====
print("\n1. Gemini 2.5 Flashにレビューを依頼中...")

try:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt}
                ] + image_contents
            }
        ],
        max_tokens=4000
    )

    gemini_review = response.choices[0].message.content
    print(f"  ✅ Geminiのレビューを取得（{len(gemini_review)}文字）")

    # 保存
    with open('gemini_senior_editor_review.md', 'w', encoding='utf-8') as f:
        f.write("# Gemini 2.5 Flash - シニア編集者レビュー\n\n")
        f.write(gemini_review)

    print("  ✅ 保存完了: gemini_senior_editor_review.md")

except Exception as e:
    print(f"  ❌ Geminiのレビュー取得に失敗: {e}")
    gemini_review = None

# ===== ChatGPT (GPT-4.1-mini) =====
print("\n2. ChatGPT (GPT-4.1-mini)にレビューを依頼中...")

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt}
                ] + image_contents
            }
        ],
        max_tokens=4000
    )

    chatgpt_review = response.choices[0].message.content
    print(f"  ✅ ChatGPTのレビューを取得（{len(chatgpt_review)}文字）")

    # 保存
    with open('chatgpt_senior_editor_review.md', 'w', encoding='utf-8') as f:
        f.write("# ChatGPT (GPT-4.1-mini) - シニア編集者レビュー\n\n")
        f.write(chatgpt_review)

    print("  ✅ 保存完了: chatgpt_senior_editor_review.md")

except Exception as e:
    print(f"  ❌ ChatGPTのレビュー取得に失敗: {e}")
    chatgpt_review = None

print("\n" + "="*60)
print("✅ レビュー取得完了！")
print("="*60)
print("\n出力ファイル:")
if gemini_review:
    print("  - gemini_senior_editor_review.md")
if chatgpt_review:
    print("  - chatgpt_senior_editor_review.md")
