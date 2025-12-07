#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
v21の3つのWord文書を結合するスクリプト
"""

from docx import Document

def add_page_break(doc):
    """ページ区切りを追加"""
    doc.add_page_break()

def merge_word_documents(files, output):
    """
    複数のWord文書を結合
    
    Args:
        files: 結合するファイルのリスト
        output: 出力ファイル名
    """
    # 最初のファイルを基準として読み込み
    merged_doc = Document(files[0])
    
    # 2つ目以降のファイルを追加
    for file in files[1:]:
        # ページ区切りを追加
        add_page_break(merged_doc)
        
        # ファイルを読み込み
        doc = Document(file)
        
        # すべての要素をコピー
        for element in doc.element.body:
            merged_doc.element.body.append(element)
    
    # 保存
    merged_doc.save(output)
    print(f"結合完了: {output}")

if __name__ == "__main__":
    files = [
        "v21_part1.docx",
        "v21_part2.docx",
        "v21_part3.docx"
    ]
    
    output = "complete_manuscript_v21_final.docx"
    
    merge_word_documents(files, output)
