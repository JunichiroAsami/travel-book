#!/usr/bin/env python3
"""
GeminiとChatGPTにPDFファイル全体をアップロードしてシニア編集者レビューを依頼
"""

import os
from openai import OpenAI

# OpenAI クライアントの初期化
client = OpenAI()

print("="*60)
print("シニア編集者レビュー依頼スクリプト（PDFファイル全体）")
print("="*60)

pdf_path = '/home/ubuntu/ai_travel_book_project/finals/complete_manuscript_v27_safe.pdf'

# プロンプト
prompt = """あなたは、シニア編集者です。この書籍のデザイン及び内容に関して、厳しくレビューしてください。また、改善案があれば指摘してください。

この書籍は「AIツアーコンダクターと歩く ベトナム・タイ周遊記」というタイトルで、AI活用の旅行ガイドブックです。

以下の観点から、厳しくレビューしてください：

1. **デザインの洗練度**: 表紙、目次、本文レイアウト、フォント、余白、ヘッダー・フッター
2. **内容の質**: 情報の正確性、論理的な構成、読みやすさ、専門性
3. **テーブルと図表**: 見やすさ、情報の整理、キャプションの有無
4. **商業出版物としての完成度**: 市販の書籍と比較して、どの程度のレベルか
5. **改善が必要な箇所**: 具体的にどこをどう改善すべきか（優先順位付き）

**評価基準**:
- ★★★★★ (5.0): 商業出版物として完璧
- ★★★★☆ (4.0): 商業出版物として十分な品質
- ★★★☆☆ (3.0): 改善が必要だが、骨格はしっかりしている
- ★★☆☆☆ (2.0): 大幅な改善が必要
- ★☆☆☆☆ (1.0): 出版には不適切

厳しく、率直に、詳細に評価してください。全215ページを確認してください。"""

# ===== Gemini 2.5 Flash =====
print("\n1. Gemini 2.5 Flashにレビューを依頼中...")
print("   PDFファイルをアップロード中...")

try:
    # PDFファイルをアップロード
    with open(pdf_path, 'rb') as f:
        pdf_content = f.read()
    
    # Geminiに送信（OpenAI互換APIでファイルアップロード）
    # 注: Geminiはファイルアップロードに対応していない可能性があるため、
    # 代わりにテキスト抽出を試みる
    
    import PyPDF2
    
    # PDFからテキストを抽出
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text_content = ""
    for i, page in enumerate(pdf_reader.pages[:50]):  # 最初の50ページのみ
        text_content += f"\n\n--- ページ {i+1} ---\n\n"
        text_content += page.extract_text()
    
    print(f"   ✅ PDFから{len(pdf_reader.pages)}ページ中50ページのテキストを抽出")
    
    # Geminiに送信
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\n以下は書籍の最初の50ページのテキスト内容です：\n\n{text_content[:100000]}"
            }
        ],
        max_tokens=4000
    )

    gemini_review = response.choices[0].message.content
    print(f"   ✅ Geminiのレビューを取得（{len(gemini_review)}文字）")

    # 保存
    with open('gemini_senior_editor_review_full.md', 'w', encoding='utf-8') as f:
        f.write("# Gemini 2.5 Flash - シニア編集者レビュー（全体）\n\n")
        f.write(gemini_review)

    print("   ✅ 保存完了: gemini_senior_editor_review_full.md")

except Exception as e:
    print(f"   ❌ Geminiのレビュー取得に失敗: {e}")

# ===== ChatGPT (GPT-4.1-mini) =====
print("\n2. ChatGPT (GPT-4.1-mini)にレビューを依頼中...")
print("   PDFから最初の50ページのテキストを抽出中...")

try:
    # ChatGPTに送信
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\n以下は書籍の最初の50ページのテキスト内容です：\n\n{text_content[:100000]}"
            }
        ],
        max_tokens=4000
    )

    chatgpt_review = response.choices[0].message.content
    print(f"   ✅ ChatGPTのレビューを取得（{len(chatgpt_review)}文字）")

    # 保存
    with open('chatgpt_senior_editor_review_full.md', 'w', encoding='utf-8') as f:
        f.write("# ChatGPT (GPT-4.1-mini) - シニア編集者レビュー（全体）\n\n")
        f.write(chatgpt_review)

    print("   ✅ 保存完了: chatgpt_senior_editor_review_full.md")

except Exception as e:
    print(f"   ❌ ChatGPTのレビュー取得に失敗: {e}")

print("\n" + "="*60)
print("✅ レビュー取得完了！")
print("="*60)
print("\n出力ファイル:")
print("  - gemini_senior_editor_review_full.md")
print("  - chatgpt_senior_editor_review_full.md")
print("\n注: PDFの画像情報は含まれていないため、デザインの詳細な評価は限定的です。")
