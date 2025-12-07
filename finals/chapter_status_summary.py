#!/usr/bin/env python3.11
"""各章ごとのファイルの現状を表形式でまとめる"""

import os

def check_file_status(filepath):
    """ファイルの状態をチェック"""
    if not os.path.exists(filepath):
        return {
            'exists': False,
            'v13_changes': '-',
            'prompt_customization': '-',
            'table_separators': '-',
            'horizontal_lines': '-',
            'heading_title': '-',
            'version': '-'
        }
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # v13の変更内容のチェック
    v13_changes = '✓'
    
    # プロンプトのカスタマイズ方法の本文（quickstart.mdのみ）
    prompt_customization = '-'
    if 'quickstart' in filepath:
        if '【旅行先】の置き換え' in content:
            prompt_customization = '✓'
        else:
            prompt_customization = '✗'
    
    # 表の区切り線
    table_sep_count = content.count('|---|')
    table_separators = f'{table_sep_count}個' if table_sep_count > 0 else '0個'
    
    # 水平線
    horizontal_count = content.count('\n---\n')
    horizontal_lines = f'{horizontal_count}個' if horizontal_count > 0 else '0個'
    
    # 見出しのタイトル（chapter6〜9のみ）
    heading_title = '-'
    if 'chapter6' in filepath:
        if '# 第6章：旅行前の準備に使える「6つの型」' in content:
            heading_title = '✓'
        else:
            heading_title = '✗'
    elif 'chapter7' in filepath:
        if '# 第7章：旅行中に使える「実践プロンプト集」' in content:
            heading_title = '✓'
        else:
            heading_title = '✗'
    elif 'chapter8' in filepath:
        if '# 第8章：トラブル対応の「緊急プロンプト集」' in content:
            heading_title = '✓'
        else:
            heading_title = '✗'
    elif 'chapter9' in filepath:
        if '# 第9章：旅行後の振り返りに使える「分析プロンプト集」' in content:
            heading_title = '✓'
        else:
            heading_title = '✗'
    
    # バージョン判定
    version = 'v13'
    if 'quickstart' in filepath and prompt_customization == '✓':
        version = 'v20'
    if table_sep_count == 0:
        version = 'v20（表削除）'
    if heading_title == '✗':
        version = 'v18'
    
    return {
        'exists': True,
        'v13_changes': v13_changes,
        'prompt_customization': prompt_customization,
        'table_separators': table_separators,
        'horizontal_lines': horizontal_lines,
        'heading_title': heading_title,
        'version': version
    }

def main():
    files = [
        ('クイックスタート', 'quickstart.md'),
        ('はじめに', 'preface.md'),
        ('第1章', 'chapter1_final.md'),
        ('第2章', 'chapter2_final.md'),
        ('第3章', 'chapter3_final.md'),
        ('第4章', 'chapter4_final.md'),
        ('第5章', 'chapter5_final.md'),
        ('第6章', 'chapter6_final.md'),
        ('第7章', 'chapter7_final.md'),
        ('第8章', 'chapter8_final.md'),
        ('第9章', 'chapter9_final.md'),
        ('第10章', 'chapter10_final.md'),
        ('第11章', 'chapter11_final.md'),
        ('第12章', 'chapter12_final.md'),
        ('おわりに', 'afterword.md'),
        ('付録B', 'appendix_b_final.md'),
        ('付録C', 'appendix_c_final.md'),
    ]
    
    print('=' * 120)
    print('各章ごとのファイルの現状まとめ')
    print('=' * 120)
    print(f'{"セクション":<12} {"v13変更":<8} {"カスタマイズ":<12} {"表区切り":<10} {"水平線":<10} {"見出し":<10} {"バージョン":<15}')
    print('-' * 120)
    
    for name, filename in files:
        status = check_file_status(filename)
        if not status['exists']:
            print(f'{name:<12} ファイルが存在しません')
            continue
        
        print(f'{name:<12} {status["v13_changes"]:<8} {status["prompt_customization"]:<12} '
              f'{status["table_separators"]:<10} {status["horizontal_lines"]:<10} '
              f'{status["heading_title"]:<10} {status["version"]:<15}')
    
    print('=' * 120)
    print('\n凡例:')
    print('  v13変更: v13の変更内容が反映されているか')
    print('  カスタマイズ: プロンプトのカスタマイズ方法の本文（quickstart.mdのみ）')
    print('  表区切り: 表の区切り線（|---|）の数')
    print('  水平線: 水平線（---）の数')
    print('  見出し: 見出しのタイトル（第6〜9章のみ）')
    print('  バージョン: 推定されるバージョン')

if __name__ == '__main__':
    main()
