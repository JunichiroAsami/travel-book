#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
17個の標準スタイルWord文書を結合するスクリプト
"""

from docx import Document

def merge_std_chapters(files, output):
    """
    17個のWord文書を結合
    
    Args:
        files: 結合するファイルのリスト
        output: 出力ファイル名
    """
    # 最初のファイルを基準として読み込み
    merged_doc = Document(files[0])
    
    # 2つ目以降のファイルを追加
    for file in files[1:]:
        # ページ区切りを追加
        merged_doc.add_page_break()
        
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
        "quickstart_std.docx",
        "preface_std.docx",
        "chapter1_final_std.docx",
        "chapter2_final_std.docx",
        "chapter3_final_std.docx",
        "chapter4_final_std.docx",
        "chapter5_final_std.docx",
        "chapter6_final_std.docx",
        "chapter7_final_std.docx",
        "chapter8_final_std.docx",
        "chapter9_final_std.docx",
        "chapter10_final_std.docx",
        "chapter11_final_std.docx",
        "chapter12_final_std.docx",
        "afterword_std.docx",
        "appendix_b_final_std.docx",
        "appendix_c_final_std.docx"
    ]
    
    output = "complete_manuscript_v21_final.docx"
    
    merge_std_chapters(files, output)
