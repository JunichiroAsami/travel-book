#!/usr/bin/env python3
"""
用語の表記ゆれを修正するスクリプト
"""

import os
import re

# 修正対象のファイルリスト
files = [
    'quickstart.md',
    'introduction_final.md',
    'chapter1_final.md',
    'chapter2_final.md',
    'chapter3_final.md',
    'chapter4_final.md',
    'chapter5_final.md',
    'chapter6_final.md',
    'chapter7_final.md',
    'chapter8_final.md',
    'chapter9_final.md',
    'chapter10_final.md',
    'chapter11_final.md',
    'chapter12_final.md',
    'afterword.md',
    'appendix_b_final.md',
    'appendix_c_final.md',
]

# 修正パターン
replacements = [
    # AIの表記ゆれ（単語境界を考慮）
    (r'\bai\b', 'AI'),  # 小文字のai
    (r'\bAi\b', 'AI'),  # Ai
    
    # バンコクの表記ゆれ
    (r'Bangkok', 'バンコク'),
    
    # ホーチミンの表記ゆれ
    (r'ホーチミン市', 'ホーチミン'),
]

total_replacements = 0

for filename in files:
    if not os.path.exists(filename):
        print(f"⚠️ ファイルが見つかりません: {filename}")
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    file_replacements = 0
    
    for pattern, replacement in replacements:
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, replacement, content)
            file_replacements += matches
            print(f"  {filename}: '{pattern}' → '{replacement}' ({matches}箇所)")
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        total_replacements += file_replacements
        print(f"✅ {filename}: {file_replacements}箇所を修正")
    else:
        print(f"  {filename}: 修正なし")

print(f"\n合計: {total_replacements}箇所を修正しました")
