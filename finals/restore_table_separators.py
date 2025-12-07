#!/usr/bin/env python3.11
"""
削除した表の区切り線を復元するスクリプト
v13から表の構造を抽出して、章ごとのファイルに復元する
"""

import re
import os

# v13のファイルから表を抽出
with open('complete_manuscript_v13_fixed.md', 'r', encoding='utf-8') as f:
    v13_content = f.read()

# 表のパターンを検索（ヘッダー行 + 区切り線 + データ行）
table_pattern = re.compile(
    r'(\|[^\n]+\|)\n'  # ヘッダー行
    r'(\|[\s\-:]+\|)\n'  # 区切り線
    r'((?:\|[^\n]+\|\n?)+)',  # データ行（複数）
    re.MULTILINE
)

# v13から表を抽出
v13_tables = []
for match in table_pattern.finditer(v13_content):
    header = match.group(1)
    separator = match.group(2)
    data = match.group(3)
    v13_tables.append({
        'header': header,
        'separator': separator,
        'data': data,
        'full': match.group(0)
    })

print(f"v13から{len(v13_tables)}個の表を抽出しました")
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
for file in chapter_files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 表のヘッダー行を検索（区切り線がない表）
    # パターン: ヘッダー行の直後にデータ行がある（区切り線がない）
    broken_table_pattern = re.compile(
        r'(\|[^\n]+\|)\n'  # ヘッダー行
        r'(\|[^\n\-:]+\|)',  # データ行（区切り線ではない）
        re.MULTILINE
    )
    
    restored_count = 0
    for match in broken_table_pattern.finditer(content):
        header = match.group(1).strip()
        
        # v13から対応する表を検索
        for table in v13_tables:
            if table['header'].strip() == header:
                # 区切り線を挿入
                original = match.group(0)
                restored = f"{table['header']}\n{table['separator']}\n{match.group(2)}"
                content = content.replace(original, restored, 1)
                restored_count += 1
                break
    
    if restored_count > 0:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file}: {restored_count}個の表の区切り線を復元")

print()
print("=" * 80)
print("✓ 表の区切り線の復元が完了しました")
print("=" * 80)
