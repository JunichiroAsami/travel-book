#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第6章の階層番号統一スクリプト
- 型をグループ化（6.1. 情報収集と計画作成の型、6.2. 現地サービス活用の型）
- 「✅ 成功事例1」→「実例」に変更、✅を削除
- LOG番号はタイトルから削除
- すべての項に階層番号を振る（6.x.x.）
- 「章全体のまとめ」「次のステップ」「この章のまとめ」「次章への案内」に節レベルで番号を振る
"""

import re

def update_chapter6_hierarchy(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    updated_lines = []
    
    current_section = 0
    current_subsection = 0
    current_subsubsection = 0
    in_code_block = False
    
    # 型番号から節・項番号へのマッピング
    type_to_section = {
        '型1': (1, 1),  # 6.1.1
        '型2': (1, 2),  # 6.1.2
        '型3': (1, 3),  # 6.1.3
        '型4': (2, 1),  # 6.2.1
        '型5': (2, 2),  # 6.2.2
        '型6': (2, 3),  # 6.2.3
    }
    
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
        
        # 第3部の導入はそのまま
        if line.startswith('## 第3部：'):
            updated_lines.append(line)
            continue
        
        # 「章の導入」は削除（本文はそのまま）
        if line == '## 章の導入':
            continue
        
        # 型レベル（##）の変更
        if line.startswith('## 型'):
            # 型番号を抽出（例：「型1」）
            match = re.match(r'## (型\d+)：(.+)', line)
            if match:
                type_num = match.group(1)
                title = match.group(2)
                
                # LOG番号を削除
                title = re.sub(r'（LOG\d+）', '', title).strip()
                
                # 型番号から節・項番号を取得
                if type_num in type_to_section:
                    section, subsection = type_to_section[type_num]
                    
                    # 節が変わったら、グループ見出しを挿入
                    if section != current_section:
                        current_section = section
                        current_subsection = 0
                        current_subsubsection = 0
                        
                        if section == 1:
                            updated_lines.append(f'## 6.1. 情報収集と計画作成の型')
                            updated_lines.append('')
                        elif section == 2:
                            updated_lines.append(f'## 6.2. 現地サービス活用の型')
                            updated_lines.append('')
                    
                    # 項レベルの見出しを追加
                    current_subsection = subsection
                    current_subsubsection = 0
                    updated_lines.append(f'### 6.{section}.{subsection}. {title}')
                    continue
        
        # 「章全体のまとめ」「次のステップ」「この章のまとめ」「次章への案内」に節レベルで番号を振る
        if line == '## 章全体のまとめ':
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            updated_lines.append(f'## 6.{current_section}. 章全体のまとめ')
            continue
        
        if line.startswith('## 次のステップ：'):
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            title = line.replace('## 次のステップ：', '')
            updated_lines.append(f'## 6.{current_section}. 次のステップ：{title}')
            continue
        
        if line == '## この章のまとめ':
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            updated_lines.append(f'## 6.{current_section}. この章のまとめ')
            continue
        
        if line == '## 次章への案内':
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            updated_lines.append(f'## 6.{current_section}. 次章への案内')
            continue
        
        # 項レベル（###）の変更（current_section > 0の場合のみ）
        if line.startswith('### ') and current_section > 0:
            current_subsubsection += 1
            
            # 「### ✅ 成功事例1：ホーチミンガイド作成（LOG005）」→「### 6.x.x.x. 実例：ホーチミンガイド作成」
            if '✅ 成功事例' in line:
                # LOG番号を削除
                title = re.sub(r'### ✅ 成功事例\d+：', '', line)
                title = re.sub(r'（LOG\d+）', '', title).strip()
                updated_lines.append(f'#### 6.{current_section}.{current_subsection}.{current_subsubsection}. 実例：{title}')
            # 「### 実例：観光スポット巡り提案（LOG010）」→「### 6.x.x.x. 実例：観光スポット巡り提案」
            elif line.startswith('### 実例：'):
                title = re.sub(r'### 実例：', '', line)
                title = re.sub(r'（LOG\d+）', '', title).strip()
                updated_lines.append(f'#### 6.{current_section}.{current_subsection}.{current_subsubsection}. 実例：{title}')
            # 「### 導入部」「### 型のテンプレート」「### 使い方のポイント」
            elif line in ['### 導入部', '### 型のテンプレート', '### 使い方のポイント']:
                title = line.replace('### ', '')
                updated_lines.append(f'#### 6.{current_section}.{current_subsection}.{current_subsubsection}. {title}')
            # 「### ステップ1：...」
            elif line.startswith('### ステップ'):
                title = line.replace('### ', '')
                updated_lines.append(f'### 6.{current_section}.{current_subsubsection}. {title}')
            # その他の項
            else:
                title = line.replace('### ', '')
                updated_lines.append(f'### 6.{current_section}.{current_subsubsection}. {title}')
            continue
        
        # その他の行はそのまま
        updated_lines.append(line)
    
    # ファイルに書き込み
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))
    
    print(f'第6章の階層番号統一が完了しました: {output_file}')
    print(f'- 節数: {current_section}')

if __name__ == '__main__':
    input_file = '/home/ubuntu/ai_travel_book_project/finals/chapter6_final.md'
    output_file = '/home/ubuntu/ai_travel_book_project/finals/chapter6_final.md'
    update_chapter6_hierarchy(input_file, output_file)
