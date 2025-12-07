#!/bin/bash
# 17個の個別MDファイルから目次付きのWord文書を作成

set -e

echo "================================================================================"
echo "17個の個別MDファイルから目次付きのWord文書を作成"
echo "================================================================================"
echo

# 参照文書
REF_DOC="complete_manuscript_v10.docx"

# 章のリスト
CHAPTERS=(
    "quickstart.md"
    "preface.md"
    "chapter1_final.md"
    "chapter2_final.md"
    "chapter3_final.md"
    "chapter4_final.md"
    "chapter5_final.md"
    "chapter6_final.md"
    "chapter7_final.md"
    "chapter8_final.md"
    "chapter9_final.md"
    "chapter10_final.md"
    "chapter11_final.md"
    "chapter12_final.md"
    "afterword.md"
    "appendix_b_final.md"
    "appendix_c_final.md"
)

# 統合マークダウンを作成（目次用のプレースホルダーを追加）
echo "統合マークダウンを作成中..."
cat > complete_manuscript_v21_with_toc.md << 'EOF'
---
toc: true
toc-depth: 2
---

EOF

# 17個の章を結合
for chapter in "${CHAPTERS[@]}"; do
    echo "  ✓ $chapter を追加"
    cat "$chapter" >> complete_manuscript_v21_with_toc.md
    echo "" >> complete_manuscript_v21_with_toc.md
    echo "" >> complete_manuscript_v21_with_toc.md
done

echo "✓ 統合マークダウンを作成しました"
echo

# Pandocで変換（目次付き）
echo "Pandocで変換中（目次付き）..."
pandoc complete_manuscript_v21_with_toc.md \
    -o complete_manuscript_v21_final.docx \
    --reference-doc="$REF_DOC" \
    --toc \
    --toc-depth=2

echo "✓ 変換完了"
echo

# 検証
echo "================================================================================"
echo "検証"
echo "================================================================================"
python3.11 << 'PYTHON_EOF'
from docx import Document

doc = Document("complete_manuscript_v21_final.docx")

heading1_count = sum(1 for para in doc.paragraphs if para.style.name == 'Heading 1')
heading2_count = sum(1 for para in doc.paragraphs if para.style.name == 'Heading 2')
heading3_count = sum(1 for para in doc.paragraphs if para.style.name == 'Heading 3')

print(f"見出し1の数: {heading1_count}")
print(f"見出し2の数: {heading2_count}")
print(f"見出し3の数: {heading3_count}")
print(f"総段落数: {len(doc.paragraphs):,}")
print(f"セクション数: {len(doc.sections)}")

# 見出し1のリスト
heading1_list = [p.text for p in doc.paragraphs if p.style.name == 'Heading 1']
print()
print("見出し1の一覧:")
for i, title in enumerate(heading1_list, start=1):
    print(f"  {i:2}. {title}")
PYTHON_EOF

echo
echo "================================================================================"
echo "完了: complete_manuscript_v21_final.docx"
echo "================================================================================"
