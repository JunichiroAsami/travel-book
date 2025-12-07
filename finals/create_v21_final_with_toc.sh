#!/bin/bash
# 17個の個別MDファイルから目次付きのWord文書を作成（v19と同じ方法）

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

# 各章をPandocでWord変換
echo "各章をPandocでWord変換中..."
for i in "${!CHAPTERS[@]}"; do
    chapter="${CHAPTERS[$i]}"
    output="chapter_$(printf "%02d" $i).docx"
    
    pandoc "$chapter" -o "$output" --reference-doc="$REF_DOC"
    echo "  ✓ $chapter → $output"
done

echo "✓ すべての章をWord変換しました"
echo

# Python で結合と目次追加
python3.11 << 'PYTHON_EOF'
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

print("17個のWord文書を結合中...")

# 最初のファイルを読み込み
doc = Document("chapter_00.docx")
print("✓ chapter_00.docx を読み込みました")

# ページ番号の開始を1に設定
if len(doc.sections) > 0:
    sectPr = doc.sections[0]._sectPr
    pgNumType = sectPr.find(qn('w:pgNumType'))
    if pgNumType is None:
        pgNumType = OxmlElement('w:pgNumType')
        sectPr.append(pgNumType)
    pgNumType.set(qn('w:start'), '1')
    print("✓ ページ番号の開始を1に設定しました")

# 残りのファイルを追加
for i in range(1, 17):
    chapter_file = f"chapter_{i:02d}.docx"
    chapter_doc = Document(chapter_file)
    
    for element in chapter_doc.element.body:
        doc.element.body.append(element)
    
    print(f"✓ {chapter_file} を追加しました")

# 見出しを抽出（目次用）
headings = []
for para in doc.paragraphs:
    if para.style.name == 'Heading 1':
        headings.append((1, para.text))
    elif para.style.name == 'Heading 2':
        headings.append((2, para.text))

print(f"✓ 見出しを抽出しました（見出し1: {sum(1 for h in headings if h[0] == 1)}個、見出し2: {sum(1 for h in headings if h[0] == 2)}個）")

# 目次を先頭に挿入
print()
print("目次を先頭に挿入中...")

# 目次タイトルを作成
toc_title_para = OxmlElement('w:p')
toc_title_pPr = OxmlElement('w:pPr')

# 中央揃え
jc = OxmlElement('w:jc')
jc.set(qn('w:val'), 'center')
toc_title_pPr.append(jc)

# 背景色を青に設定
shd = OxmlElement('w:shd')
shd.set(qn('w:fill'), '00B0F0')
toc_title_pPr.append(shd)

toc_title_para.append(toc_title_pPr)

# タイトルのテキスト
toc_title_run = OxmlElement('w:r')
toc_title_rPr = OxmlElement('w:rPr')
sz = OxmlElement('w:sz')
sz.set(qn('w:val'), '32')  # 16pt
szCs = OxmlElement('w:szCs')
szCs.set(qn('w:val'), '32')
b = OxmlElement('w:b')
toc_title_rPr.append(sz)
toc_title_rPr.append(szCs)
toc_title_rPr.append(b)
toc_title_run.append(toc_title_rPr)

toc_title_text = OxmlElement('w:t')
toc_title_text.text = "TABLE OF CONTENTS"
toc_title_run.append(toc_title_text)

toc_title_para.append(toc_title_run)

# 先頭に挿入
doc.element.body.insert(0, toc_title_para)

print("✓ 目次タイトルを追加しました")

# 目次エントリを追加（見出し2まで、最初の60個）
for level, text in headings[:60]:
    toc_entry_para = OxmlElement('w:p')
    toc_entry_run = OxmlElement('w:r')
    toc_entry_rPr = OxmlElement('w:rPr')
    
    if level == 1:
        # 見出し1: ボールド、11pt
        b = OxmlElement('w:b')
        toc_entry_rPr.append(b)
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), '22')  # 11pt
        szCs = OxmlElement('w:szCs')
        szCs.set(qn('w:val'), '22')
        toc_entry_rPr.append(sz)
        toc_entry_rPr.append(szCs)
        toc_text = text
    else:
        # 見出し2: 通常、10pt、インデント
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), '20')  # 10pt
        szCs = OxmlElement('w:szCs')
        szCs.set(qn('w:val'), '20')
        toc_entry_rPr.append(sz)
        toc_entry_rPr.append(szCs)
        toc_text = f"  {text}"
    
    toc_entry_run.append(toc_entry_rPr)
    toc_entry_text = OxmlElement('w:t')
    toc_entry_text.text = toc_text
    toc_entry_run.append(toc_entry_text)
    toc_entry_para.append(toc_entry_run)
    
    doc.element.body.insert(len(headings[:60]) - headings[:60].index((level, text)), toc_entry_para)

print(f"✓ 目次エントリを追加しました（{min(60, len(headings))}個）")

# ページ区切りを目次の後に追加
page_break_para = OxmlElement('w:p')
page_break_run = OxmlElement('w:r')
page_break_br = OxmlElement('w:br')
page_break_br.set(qn('w:type'), 'page')
page_break_run.append(page_break_br)
page_break_para.append(page_break_run)
doc.element.body.insert(min(60, len(headings)) + 1, page_break_para)

print("✓ ページ区切りを追加しました")

# 保存
output_file = "complete_manuscript_v21_final.docx"
doc.save(output_file)

print()
print("=" * 80)
print(f"✓ 完了: {output_file}")
print("=" * 80)

# 検証
heading1_count = sum(1 for para in doc.paragraphs if para.style.name == 'Heading 1')
heading2_count = sum(1 for para in doc.paragraphs if para.style.name == 'Heading 2')
heading3_count = sum(1 for para in doc.paragraphs if para.style.name == 'Heading 3')

print()
print("【検証結果】")
print(f"  見出し1の数: {heading1_count}")
print(f"  見出し2の数: {heading2_count}")
print(f"  見出し3の数: {heading3_count}")
print(f"  総段落数: {len(doc.paragraphs):,}")
PYTHON_EOF

echo
echo "================================================================================"
echo "完了: complete_manuscript_v21_final.docx"
echo "================================================================================"
