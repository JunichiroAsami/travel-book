#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第4章の階層番号統一スクリプト
- 「第○節：」を削除し、「4.x.」形式に変更
- 「実例1」「実例2」→「実例」に変更（番号は階層番号に統合）
- LOG番号はタイトルから削除
- すべての項に階層番号を振る（4.x.x.）
- 「まとめ」「次章への案内」に節レベルで番号を振る
"""

import re

def update_chapter4_hierarchy(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    updated_lines = []
    
    current_section = 0
    current_subsection = 0
    in_code_block = False
    
    for i, line in enumerate(lines):
        # コードブロック（```）の開始/終了を判定
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            updated_lines.append(line)
            continue
        
        # コードブロック内はそのまま
        if in_code_block:
            updated_lines.append(line)
            continue
        
        # 節レベル（##）の変更
        if line.startswith('## 第') and '節：' in line:
            current_section += 1
            current_subsection = 0
            # 「## 第1節：リアルタイムナビゲーター」→「## 4.1. リアルタイムナビゲーター」
            title = line.split('節：', 1)[1] if '節：' in line else line.replace('## 第', '').replace('節', '')
            updated_lines.append(f'## 4.{current_section}. {title}')
            continue
        
        # 「第4章のまとめ」「参考ログ」「この章のまとめ」に節レベルで番号を振る
        if line == '## 第4章のまとめ':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 4.{current_section}. 第4章のまとめ')
            continue
        
        if line == '## 参考ログ':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 4.{current_section}. 参考ログ')
            continue
        
        if line == '## この章のまとめ':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 4.{current_section}. この章のまとめ')
            continue
        
        # 項レベル（###）の変更（current_section > 0の場合のみ）
        if line.startswith('### ') and current_section > 0:
            current_subsection += 1
            
            # 「### 実例1：郊外駅の目的地（LOG014）」→「### 4.x.x. 実例：郊外駅の目的地」
            if line.startswith('### 実例'):
                # LOG番号を削除
                title = re.sub(r'### 実例\d+：', '', line)
                title = re.sub(r'（LOG\d+）', '', title).strip()
                updated_lines.append(f'### 4.{current_section}.{current_subsection}. 実例：{title}')
            # 「### まとめ」
            elif line == '### まとめ':
                updated_lines.append(f'### 4.{current_section}.{current_subsection}. まとめ')
            # 「### 本章で学んだこと」「### 次章への案内」「### 実践のヒント」
            elif line in ['### 本章で学んだこと', '### 次章への案内', '### 実践のヒント']:
                title = line.replace('### ', '')
                updated_lines.append(f'### 4.{current_section}.{current_subsection}. {title}')
            # その他の項
            else:
                title = line.replace('### ', '')
                updated_lines.append(f'### 4.{current_section}.{current_subsection}. {title}')
            continue
        
        # その他の行はそのまま
        updated_lines.append(line)
    
    # ファイルに書き込み
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))
    
    print(f'第4章の階層番号統一が完了しました: {output_file}')
    print(f'- 節数: {current_section}')

if __name__ == '__main__':
    input_file = '/home/ubuntu/ai_travel_book_project/finals/chapter4_final.md'
    output_file = '/home/ubuntu/ai_travel_book_project/finals/chapter4_final.md'
    update_chapter4_hierarchy(input_file, output_file)
