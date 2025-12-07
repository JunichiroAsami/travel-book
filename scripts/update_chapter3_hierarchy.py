#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第3章の階層番号統一スクリプト
- 「第○節：」を削除し、「3.x.」形式に変更
- 「✅ 成功事例」→「実例」に変更、✅を削除
- すべての項に階層番号を振る（3.x.x.）
- 「まとめ」「次章への案内」に節レベルで番号を振る
"""

import re

def update_chapter3_hierarchy(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    updated_lines = []
    
    current_section = 0
    current_subsection = 0
    in_prompt_block = False
    
    for i, line in enumerate(lines):
        # プロンプトブロック内かどうかを判定
        if line.strip().startswith('```'):
            in_prompt_block = not in_prompt_block
            updated_lines.append(line)
            continue
        
        # プロンプトブロック内はそのまま
        if in_prompt_block:
            updated_lines.append(line)
            continue
        
        # 第2部の導入はそのまま
        if line.startswith('## 第2部：'):
            updated_lines.append(line)
            continue
        
        # 節レベル（##）の変更
        if line.startswith('## 第') and '節：' in line:
            current_section += 1
            current_subsection = 0
            # 「## 第1節：曖昧な願望を「現実的なプラン」に変える」→「## 3.1. 曖昧な願望を「現実的なプラン」に変える」
            title = line.split('節：', 1)[1] if '節：' in line else line.replace('## 第', '').replace('節', '')
            updated_lines.append(f'## 3.{current_section}. {title}')
            continue
        
        # 「参考ログ」「この章のまとめ」に節レベルで番号を振る
        if line == '## 参考ログ':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 3.{current_section}. 参考ログ')
            continue
        
        if line == '## この章のまとめ':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 3.{current_section}. この章のまとめ')
            continue
        
        # 項レベル（###）の変更
        if line.startswith('### ') and current_section > 0:
            current_subsection += 1
            
            # 「### ✅ 成功事例：...」→「### 3.x.x. 実例：...」
            if '✅ 成功事例：' in line:
                title = line.replace('### ✅ 成功事例：', '')
                updated_lines.append(f'### 3.{current_section}.{current_subsection}. 実例：{title}')
            # 「### ストーリー：...」→「### 3.x.x. 実例：...」
            elif 'ストーリー：' in line:
                title = line.replace('### ストーリー：', '')
                updated_lines.append(f'### 3.{current_section}.{current_subsection}. 実例：{title}')
            # その他の項
            else:
                title = line.replace('### ', '')
                updated_lines.append(f'### 3.{current_section}.{current_subsection}. {title}')
            continue
        
        # その他の行はそのまま
        updated_lines.append(line)
    
    # ファイルに書き込み
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))
    
    print(f'第3章の階層番号統一が完了しました: {output_file}')
    print(f'- 節数: {current_section}')

if __name__ == '__main__':
    input_file = '/home/ubuntu/ai_travel_book_project/finals/chapter3_final.md'
    output_file = '/home/ubuntu/ai_travel_book_project/finals/chapter3_final.md'
    update_chapter3_hierarchy(input_file, output_file)
