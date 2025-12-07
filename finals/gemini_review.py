import os
import base64
from openai import OpenAI

# OpenAI互換のクライアントを作成（Gemini用）
client = OpenAI()

# PDFから抽出した画像のパス
pdf_images_dir = "/tmp/pdf_images/complete_manuscript_v26_with_toc"

# レビュー対象のページ（表紙、目次、本文サンプル、テーブルサンプル）
target_pages = [1, 2, 3, 10, 50, 100, 200]

# 画像をBase64エンコード
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 画像URLリストを作成
image_contents = []
for page_num in target_pages:
    image_path = f"{pdf_images_dir}/{page_num:03d}.webp"
    if os.path.exists(image_path):
        base64_image = encode_image(image_path)
        image_contents.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/webp;base64,{base64_image}"
            }
        })
        print(f"Added page {page_num}")

# Geminiにレビューを依頼
print("\nSending request to Gemini 2.5 Flash...")

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """あなたは経験豊富な書籍編集者です。以下の画像は、『AIツアーコンダクターと歩く ベトナム・タイ周遊記』という書籍のPDFから抽出したページです。

書籍の見栄えに関して、以下の観点から詳細に評価してください：

1. **表紙デザイン**：タイトル、レイアウト、視覚的魅力
2. **目次**：構成、読みやすさ、ページ番号の正確性
3. **ヘッダー・フッター**：デザイン、一貫性、ページ番号の配置
4. **本文レイアウト**：フォント、行間、余白、段落の区切り
5. **テーブル・図表**：見やすさ、枠線、キャプション
6. **全体的な印象**：プロフェッショナルさ、統一感、読みやすさ

各観点について、良い点と改善点を具体的に指摘してください。最後に、総合評価（5段階）と優先的に改善すべき3つの項目を提案してください。

日本語で回答してください。"""
                }
            ] + image_contents
        }
    ],
    max_tokens=4000,
    temperature=0.7
)

# レビュー結果を出力
review_text = response.choices[0].message.content
print("\n" + "="*60)
print("Gemini 2.5 Flash Review")
print("="*60)
print(review_text)

# ファイルに保存
with open("gemini_review_result.md", "w", encoding="utf-8") as f:
    f.write("# Gemini 2.5 Flash による書籍レビュー\n\n")
    f.write(review_text)

print("\n" + "="*60)
print("Review saved to: gemini_review_result.md")
print("="*60)

