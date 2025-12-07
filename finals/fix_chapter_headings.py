#!/usr/bin/env python3
"""
章ごとのファイルの見出しを修正するスクリプト
"""

def fix_chapter_heading(filename, chapter_num, correct_title):
    """章の見出しを修正"""
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 誤った見出し（タイトルが欠落）
    wrong_heading = f"# 第{chapter_num}章：\n**本章の使い方**"
    
    # 正しい見出し
    correct_heading = f"# 第{chapter_num}章：{correct_title}\n\n**本章の使い方**"
    
    if wrong_heading in content:
        content = content.replace(wrong_heading, correct_heading)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {filename}: 見出しを修正しました")
        return True
    else:
        print(f"  {filename}: 見出しは正しいです")
        return False

if __name__ == "__main__":
    print("=" * 80)
    print("章ごとのファイルの見出しを修正")
    print("=" * 80)
    
    chapters = [
        (6, "chapter6_final.md", "旅行前の準備に使える「6つの型」"),
        (7, "chapter7_final.md", "旅行中に使える「実践プロンプト集」"),
        (8, "chapter8_final.md", "トラブル対応の「緊急プロンプト集」"),
        (9, "chapter9_final.md", "旅行後の振り返りに使える「分析プロンプト集」")
    ]
    
    for chapter_num, filename, title in chapters:
        fix_chapter_heading(filename, chapter_num, title)
    
    print("\n" + "=" * 80)
    print("✓ 修正完了")
    print("=" * 80)
