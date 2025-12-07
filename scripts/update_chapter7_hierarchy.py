#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第7章の階層番号統一スクリプト
- 「シーン1」→「7.1.」、「シーン2」→「7.2.」など
- LOG番号はタイトルから削除
- すべての項に階層番号を振る（7.x.x.）
- 「章全体のまとめ」「次のステップ」「この章のまとめ」「次章への案内」に節レベルで番号を振る
"""

import re

def update_chapter7_hierarchy(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    updated_lines = []
    
    current_section = 0
    current_subsection = 0
    in_code_block = False
    skip_next_line = False
    
    for i, line in enumerate(lines):
        # スキップフラグが立っている場合
        if skip_next_line:
            skip_next_line = False
            continue
        
        # コードブロック（```）の開始/終了を判定
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            updated_lines.append(line)
            continue
        
        # コードブロック内はそのまま
        if in_code_block:
            updated_lines.append(line)
            continue
        
        # 「この章の位置づけ」「章の導入部」は節レベルで番号を振る
        if line == '## この章の位置づけ':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 7.{current_section}. この章の位置づけ')
            continue
        
        if line == '## 章の導入部':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 7.{current_section}. 章の導入部')
            continue
        
        # シーンレベル（##）の変更
        if line.startswith('## シーン'):
            current_section += 1
            current_subsection = 0
            # 「## シーン1：現在地確認と周辺情報検索」→「## 7.3. 現在地確認と周辺情報検索」
            title = re.sub(r'## シーン\d+：', '', line)
            updated_lines.append(f'## 7.{current_section}. {title}')
            continue
        
        # 「章全体のまとめ」「次のステップ」「この章のまとめ」「次章への案内」に節レベルで番号を振る
        if line == '## 章全体のまとめ':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 7.{current_section}. 章全体のまとめ')
            continue
        
        if line.startswith('## 次のステップ：'):
            current_section += 1
            current_subsection = 0
            title = line.replace('## 次のステップ：', '')
            updated_lines.append(f'## 7.{current_section}. 次のステップ：{title}')
            continue
        
        if line == '## この章のまとめ':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 7.{current_section}. この章のまとめ')
            continue
        
        if line == '## 次章への案内':
            current_section += 1
            current_subsection = 0
            updated_lines.append(f'## 7.{current_section}. 次章への案内')
            continue
        
        # 項レベル（###）の変更（current_section > 0の場合のみ）
        if line.startswith('### ') and current_section > 0:
            current_subsection += 1
            
            # 「### 実践プロンプト1：郊外駅周辺の観光地確認（LOG014）」→「### 7.x.x. 実践プロンプト：郊外駅周辺の観光地確認」
            if line.startswith('### 実践プロンプト'):
                # LOG番号を削除
                title = re.sub(r'### 実践プロンプト\d+：', '', line)
                title = re.sub(r'（LOG\d+）', '', title).strip()
                updated_lines.append(f'### 7.{current_section}.{current_subsection}. 実践プロンプト：{title}')
            # 「### 導入部」「### プロンプト活用のコツ」「### クイックスタート：最重要プロンプト集」
            elif line in ['### 導入部', '### プロンプト活用のコツ', '### クイックスタート：最重要プロンプト集']:
                title = line.replace('### ', '')
                updated_lines.append(f'### 7.{current_section}.{current_subsection}. {title}')
            # 「### ステップ1：...」
            elif line.startswith('### ステップ'):
                title = line.replace('### ', '')
                updated_lines.append(f'### 7.{current_section}.{current_subsection}. {title}')
            # その他の項
            else:
                title = line.replace('### ', '')
                updated_lines.append(f'### 7.{current_section}.{current_subsection}. {title}')
            continue
        
        # その他の行はそのまま
        updated_lines.append(line)
    
    # ファイルに書き込み
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))
    
    print(f'第7章の階層番号統一が完了しました: {output_file}')
    print(f'- 節数: {current_section}')

if __name__ == '__main__':
    input_file = '/home/ubuntu/ai_travel_book_project/finals/chapter7_final.md'
    output_file = '/home/ubuntu/ai_travel_book_project/finals/chapter7_final.md'
    update_chapter7_hierarchy(input_file, output_file)
