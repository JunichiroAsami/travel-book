#!/usr/bin/env python3.11
"""
v18から表の構造を抽出して、章ごとのファイルに復元するスクリプト
"""

import re
import os

# v18のファイルを読み込み
with open('complete_manuscript_v18.md', 'r', encoding='utf-8') as f:
    v18_content = f.read()

# 表のパターンを検索（ヘッダー行 + 区切り線 + データ行）
table_pattern = re.compile(
    r'(\|[^\n]+\|)\n'  # ヘッダー行
    r'(\|[\s\-:]+\|)\n'  # 区切り線
    r'((?:\|[^\n]+\|\n?)*)',  # データ行（0個以上）
    re.MULTILINE
)

# v18から表を抽出
v18_tables = {}
for match in table_pattern.finditer(v18_content):
    header = match.group(1).strip()
    separator = match.group(2).strip()
    v18_tables[header] = separator

print(f"v18から{len(v18_tables)}個の表を抽出しました")
print()

# 章ごとのファイルリスト
chapter_files = [
    'quickstart.md',
    'preface.md',
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
    'appendix_c_final.md'
]

# 各ファイルで表の区切り線を復元
total_restored = 0
for file in chapter_files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 表のヘッダー行を検索
    for header, separator in v18_tables.items():
        # ヘッダー行の直後にデータ行がある場合（区切り線がない）
        pattern = re.escape(header) + r'\n(\|[^\n\-:]+\|)'
        replacement = f"{header}\n{separator}\n\\1"
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
    
    if content != original_content:
        # 復元した表の数をカウント
        restored_count = content.count('\n|') - original_content.count('\n|')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file}: 表の区切り線を復元")
        total_restored += 1

print()
print("=" * 80)
print(f"✓ 合計{total_restored}個の表の区切り線を復元しました")
print("=" * 80)
