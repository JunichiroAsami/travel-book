#!/usr/bin/env python3.11
"""
chapter6〜9の見出しを修正するスクリプト
"""

import re

# 修正するファイルとタイトル
files_to_fix = {
    'chapter6_final.md': '旅行前の準備に使える「6つの型」',
    'chapter7_final.md': '旅行中に使える「実践プロンプト集」',
    'chapter8_final.md': 'トラブル対応の「緊急プロンプト集」',
    'chapter9_final.md': '旅行後の振り返りに使える「分析プロンプト集」'
}

for filename, title in files_to_fix.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # パターン1: # 第X章：\n**本章の使い方**：...---\nタイトル
    pattern1 = r'(# 第\d+章：)\n(\*\*本章の使い方\*\*[^\n]+)\n---\n' + re.escape(title)
    replacement1 = r'\1' + title + r'\n\n**本章の使い方**\n\n\2'
    
    new_content = re.sub(pattern1, replacement1, content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ {filename}: 見出しを修正しました")
    else:
        print(f"✗ {filename}: パターンが見つかりませんでした")
        # デバッグ用に最初の100文字を表示
        print(f"  先頭100文字: {content[:100]}")

print()
print("=" * 80)
print("✓ 修正完了")
print("=" * 80)
