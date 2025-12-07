#!/usr/bin/env python3.11
"""
章ごとのマークダウンファイルが最新の状態か確認するスクリプト
"""

import os
import re

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

# 確認項目
checks = {
    'quickstart.md': [
        ('プロンプトのカスタマイズ方法の本文', r'\*\*\[旅行先\]を自分の旅行先に置き換える\*\*'),
    ],
    'chapter2_final.md': [
        ('2.3. 第3部と付録Bの使い分け', r'2\.3\. 第3部と付録Bの使い分け'),
    ],
    'chapter6_final.md': [
        ('冒頭の案内文', r'\*\*本章の使い方\*\*'),
        ('末尾の対応表', r'本章のプロンプトを今すぐ使いたい方へ'),
    ],
    'chapter7_final.md': [
        ('冒頭の案内文', r'\*\*本章の使い方\*\*'),
        ('末尾の対応表', r'本章のプロンプトを今すぐ使いたい方へ'),
    ],
    'chapter8_final.md': [
        ('冒頭の案内文', r'\*\*本章の使い方\*\*'),
        ('末尾の対応表', r'本章のプロンプトを今すぐ使いたい方へ'),
    ],
    'chapter9_final.md': [
        ('冒頭の案内文', r'\*\*本章の使い方\*\*'),
        ('末尾の対応表', r'本章のプロンプトを今すぐ使いたい方へ'),
    ],
    'appendix_b_final.md': [
        ('第3部との違い', r'第3部との違い'),
    ],
}

# 確認結果
results = {}
all_passed = True

print("=" * 80)
print("章ごとのマークダウンファイルの最新状態確認")
print("=" * 80)
print()

# 各ファイルを確認
for file in chapter_files:
    if not os.path.exists(file):
        results[file] = {'status': 'missing', 'checks': []}
        all_passed = False
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 水平線の確認
    horizontal_lines = re.findall(r'^---$', content, re.MULTILINE)
    table_separators = re.findall(r'^\|.*---.*\|$', content, re.MULTILINE)
    
    file_checks = []
    
    # 水平線の確認
    if horizontal_lines:
        file_checks.append(('水平線（---）', False, f'{len(horizontal_lines)}個残存'))
        all_passed = False
    else:
        file_checks.append(('水平線（---）', True, '削除済み'))
    
    # 表の区切り線の確認
    if table_separators:
        file_checks.append(('表の区切り線', False, f'{len(table_separators)}個残存'))
        all_passed = False
    else:
        file_checks.append(('表の区切り線', True, '削除済み'))
    
    # ファイル固有の確認項目
    if file in checks:
        for check_name, pattern in checks[file]:
            if re.search(pattern, content):
                file_checks.append((check_name, True, '存在'))
            else:
                file_checks.append((check_name, False, '欠落'))
                all_passed = False
    
    results[file] = {'status': 'ok', 'checks': file_checks}

# 結果を表示
for file in chapter_files:
    if file not in results:
        continue
    
    if results[file]['status'] == 'missing':
        print(f"✗ {file}: ファイルが存在しません")
        continue
    
    print(f"📄 {file}")
    for check_name, passed, message in results[file]['checks']:
        status = '✓' if passed else '✗'
        print(f"  {status} {check_name}: {message}")
    print()

# サマリー
print("=" * 80)
if all_passed:
    print("✓ すべての確認項目が合格しました")
else:
    print("✗ 一部の確認項目が不合格です")
print("=" * 80)
