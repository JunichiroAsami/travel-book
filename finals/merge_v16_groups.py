#!/usr/bin/env python3
"""
4つのグループを結合するスクリプト
"""

from docx import Document

def merge_documents(group_paths, output_path):
    """複数のWord文書を結合"""
    
    # Group1を読み込み（目次付き）
    doc = Document(group_paths[0])
    print(f"✓ {group_paths[0]} を読み込みました")
    
    # Group2-4を追加
    for i, group_path in enumerate(group_paths[1:], start=2):
        group_doc = Document(group_path)
        
        # グループの内容を追加
        for element in group_doc.element.body:
            doc.element.body.append(element)
        
        print(f"✓ {group_path} を追加しました")
    
    # 保存
    doc.save(output_path)
    print(f"\n✓ 結合完了: {output_path}")

if __name__ == "__main__":
    group_paths = [
        "v16_group1.docx",
        "v16_group2.docx",
        "v16_group3.docx",
        "v16_group4.docx"
    ]
    output_path = "complete_manuscript_v16_final.docx"
    
    merge_documents(group_paths, output_path)
