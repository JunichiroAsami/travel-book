#!/usr/bin/env python3
"""
v16のPart1とPart2を結合するスクリプト
"""

from docx import Document

def merge_documents(part1_path, part2_path, output_path):
    """2つのWord文書を結合"""
    
    # Part1を読み込み
    doc1 = Document(part1_path)
    
    # Part2を読み込み
    doc2 = Document(part2_path)
    
    # Part2の内容をPart1に追加
    for element in doc2.element.body:
        doc1.element.body.append(element)
    
    # 保存
    doc1.save(output_path)
    print(f"✓ 結合完了: {output_path}")
    
    # ページ数を確認
    print(f"  - Part1のページ数: {len(doc1.sections)}")

if __name__ == "__main__":
    part1_path = "complete_manuscript_v16_part1.docx"
    part2_path = "complete_manuscript_v16_part2.docx"
    output_path = "complete_manuscript_v16_merged.docx"
    
    merge_documents(part1_path, part2_path, output_path)
