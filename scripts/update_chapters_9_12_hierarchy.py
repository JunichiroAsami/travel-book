#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第9章〜第12章の階層番号統一スクリプト
- 第9章：「分析1」→「9.1.」、「分析2」→「9.2.」など
- 第10章〜第12章：「第○節：」を削除し、「x.x.」形式に変更
- すべての項に階層番号を振る（x.x.x.）
- 「まとめ」「次章への案内」に節レベルで番号を振る
"""

import re

def update_chapter9_hierarchy(input_file, output_file):
    """第9章の階層番号統一"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    updated_lines = []
    
    current_section = 0
    current_subsection = 0
    in_code_block = False
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            updated_lines.append(line)
            continue
        
        if in_code_block:
            updated_lines.append(line)
            continue
        
        # 「この章の位置づけ」の見出しを削除
        if line == '## この章の位置づけ':
            continue
        
        # 「分析1」→「9.1.」
        if line.startswith('## 分析'):
            current_section += 1
            current_subsection = 0
            title = re.sub(r'## 分析\d+：', '', line)
            updated_lines.append(f'## 9.{current_section}. {title}')
            continue
        
        # 「まとめ：振り返りこそが、旅を資産に変える」→「9.x. まとめ：...」
        if line.startswith('## まとめ：'):
            current_section += 1
            current_subsection = 0
            title = line.replace('## まとめ：', '')
            updated_lines.append(f'## 9.{current_section}. まとめ：{title}')
            continue
        
        # 「この章のまとめ」「次章への案内」
        if line in ['## この章のまとめ', '## 次章への案内']:
            current_section += 1
            current_subsection = 0
            title = line.replace('## ', '')
            updated_lines.append(f'## 9.{current_section}. {title}')
            continue
        
        # 項レベル（###）
        if line.startswith('### ') and current_section > 0:
            current_subsection += 1
            # 「### 実例1：...」→「### 9.x.x. 実例：...」
            if line.startswith('### 実例'):
                title = re.sub(r'### 実例\d+：', '', line)
                updated_lines.append(f'### 9.{current_section}.{current_subsection}. 実例：{title}')
            else:
                title = line.replace('### ', '')
                updated_lines.append(f'### 9.{current_section}.{current_subsection}. {title}')
            continue
        
        updated_lines.append(line)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))
    
    print(f'第9章の階層番号統一が完了しました: {output_file}')

def update_chapter10_12_hierarchy(chapter_num, input_file, output_file):
    """第10章〜第12章の階層番号統一"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    updated_lines = []
    
    current_section = 0
    current_subsection = 0
    current_subsubsection = 0
    in_code_block = False
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            updated_lines.append(line)
            continue
        
        if in_code_block:
            updated_lines.append(line)
            continue
        
        # 「はじめに」「おわりに」は節レベルで番号を振る
        if line.startswith('## はじめに') or line.startswith('## おわりに'):
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            title = line.replace('## ', '')
            updated_lines.append(f'## {chapter_num}.{current_section}. {title}')
            continue
        
        # 「第○節：」を削除
        if line.startswith('## 第') and '節：' in line:
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            title = line.split('節：', 1)[1] if '節：' in line else line.replace('## 第', '').replace('節', '')
            updated_lines.append(f'## {chapter_num}.{current_section}. {title}')
            continue
        
        # その他の節レベル（##）
        if line.startswith('## '):
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            title = line.replace('## ', '')
            updated_lines.append(f'## {chapter_num}.{current_section}. {title}')
            continue
        
        # 項レベル（###）
        if line.startswith('### ') and current_section > 0:
            current_subsection += 1
            current_subsubsection = 0
            title = line.replace('### ', '')
            updated_lines.append(f'### {chapter_num}.{current_section}.{current_subsection}. {title}')
            continue
        
        # 小項レベル（####）
        if line.startswith('#### ') and current_section > 0:
            current_subsubsection += 1
            title = line.replace('#### ', '')
            updated_lines.append(f'#### {chapter_num}.{current_section}.{current_subsection}.{current_subsubsection}. {title}')
            continue
        
        updated_lines.append(line)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))
    
    print(f'第{chapter_num}章の階層番号統一が完了しました: {output_file}')

if __name__ == '__main__':
    base_path = '/home/ubuntu/ai_travel_book_project/finals'
    
    # 第9章
    update_chapter9_hierarchy(
        f'{base_path}/chapter9_final.md',
        f'{base_path}/chapter9_final.md'
    )
    
    # 第10章〜第12章
    for chapter_num in [10, 11, 12]:
        update_chapter10_12_hierarchy(
            chapter_num,
            f'{base_path}/chapter{chapter_num}_final.md',
            f'{base_path}/chapter{chapter_num}_final.md'
        )
