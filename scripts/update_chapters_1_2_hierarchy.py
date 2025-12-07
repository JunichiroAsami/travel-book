#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
第1章と第2章の階層番号統一スクリプト
"""

import re

def update_chapter1():
    """第1章の階層番号を統一"""
    with open('/home/ubuntu/ai_travel_book_project/finals/chapter1_final.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # プロンプトブロック内かどうかを判定
    in_prompt = False
    lines = content.split('\n')
    new_lines = []
    
    section_count = 0
    subsection_count = 0
    
    for line in lines:
        # プロンプトブロックの開始・終了を検出
        if line.strip().startswith('```'):
            in_prompt = not in_prompt
            new_lines.append(line)
            continue
        
        # プロンプトブロック内は変更しない
        if in_prompt:
            new_lines.append(line)
            continue
        
        # 章タイトルはそのまま
        if line.startswith('# 第1章'):
            new_lines.append(line)
            continue
        
        # 節レベル（##）
        if line.startswith('## '):
            section_count += 1
            subsection_count = 0
            title = re.sub(r'^## ', '', line)
            new_lines.append(f'## 1.{section_count}. {title}')
            continue
        
        # 項レベル（###）
        if line.startswith('### '):
            subsection_count += 1
            title = re.sub(r'^### ', '', line)
            new_lines.append(f'### 1.{section_count}.{subsection_count}. {title}')
            continue
        
        new_lines.append(line)
    
    with open('/home/ubuntu/ai_travel_book_project/finals/chapter1_final.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print(f"第1章の階層番号統一完了: {section_count}節")

def update_chapter2():
    """第2章の階層番号を統一"""
    with open('/home/ubuntu/ai_travel_book_project/finals/chapter2_final.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # プロンプトブロック内かどうかを判定
    in_prompt = False
    lines = content.split('\n')
    new_lines = []
    
    section_count = 0
    subsection_count = 0
    subsubsection_count = 0
    
    for line in lines:
        # プロンプトブロックの開始・終了を検出
        if line.strip().startswith('```'):
            in_prompt = not in_prompt
            new_lines.append(line)
            continue
        
        # プロンプトブロック内は変更しない
        if in_prompt:
            new_lines.append(line)
            continue
        
        # 章タイトルはそのまま
        if line.startswith('# 第2章'):
            new_lines.append(line)
            continue
        
        # 節レベル（##）
        if line.startswith('## '):
            section_count += 1
            subsection_count = 0
            subsubsection_count = 0
            title = re.sub(r'^## ', '', line)
            new_lines.append(f'## 2.{section_count}. {title}')
            continue
        
        # 項レベル（###）
        if line.startswith('### '):
            subsection_count += 1
            subsubsection_count = 0
            title = re.sub(r'^### ', '', line)
            new_lines.append(f'### 2.{section_count}.{subsection_count}. {title}')
            continue
        
        # 小項レベル（####）
        if line.startswith('#### '):
            subsubsection_count += 1
            title = re.sub(r'^#### ', '', line)
            new_lines.append(f'#### 2.{section_count}.{subsection_count}.{subsubsection_count}. {title}')
            continue
        
        new_lines.append(line)
    
    with open('/home/ubuntu/ai_travel_book_project/finals/chapter2_final.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print(f"第2章の階層番号統一完了: {section_count}節")

if __name__ == '__main__':
    update_chapter1()
    update_chapter2()
    print("完了")
