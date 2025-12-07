#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第8章の階層番号統一スクリプト（最終版）
- 「この章の位置づけ」「章の導入部」の見出しを削除（本文は残す）
- トラブルをグループ化（8.1. 現地でのトラブル対応、8.2. 帰国後のトラブル対応）
- LOG番号はタイトルから削除
- すべての項に階層番号を振る（8.x.x.）
- 「章全体のまとめ」「次のステップ」「この章のまとめ」「次章への案内」に節レベルで番号を振る
"""

import re

def update_chapter8_hierarchy(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    updated_lines = []
    
    current_section = 0
    current_subsection = 0
    current_subsubsection = 0
    in_code_block = False
    group_inserted = {1: False, 2: False}  # グループ見出しの挿入状態を追跡
    
    # トラブル番号から節・項番号へのマッピング
    trouble_to_section = {
        'トラブル1': (1, 1),  # 8.1.1 健康トラブル
        'トラブル2': (1, 2),  # 8.1.2 ぼったくりトラブル
        'トラブル4': (1, 3),  # 8.1.3 サービストラブル
        'トラブル3': (2, 1),  # 8.2.1 荷物トラブル
        'トラブル5': (2, 2),  # 8.2.2 保険請求手続き
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
        
        # 「この章の位置づけ」「章の導入部」の見出しを削除（本文は残す）
        if line in ['## この章の位置づけ', '## 章の導入部']:
            continue
        
        # トラブルレベル（##）の変更
        if line.startswith('## トラブル'):
            # トラブル番号を抽出（例：「トラブル1」）
            match = re.match(r'## (トラブル\d+)：(.+)', line)
            if match:
                trouble_num = match.group(1)
                title = match.group(2)
                
                # LOG番号を削除
                title = re.sub(r'（LOG\d+）', '', title).strip()
                
                # トラブル番号から節・項番号を取得
                if trouble_num in trouble_to_section:
                    section, subsection = trouble_to_section[trouble_num]
                    
                    # 節が変わったら、グループ見出しを挿入（まだ挿入されていない場合のみ）
                    if not group_inserted[section]:
                        current_section = section
                        current_subsection = 0
                        current_subsubsection = 0
                        group_inserted[section] = True
                        
                        if section == 1:
                            updated_lines.append(f'## 8.{section}. 現地でのトラブル対応')
                            updated_lines.append('')
                        elif section == 2:
                            updated_lines.append(f'## 8.{section}. 帰国後のトラブル対応')
                            updated_lines.append('')
                    
                    # 項レベルの見出しを追加
                    current_subsection = subsection
                    current_subsubsection = 0
                    updated_lines.append(f'### 8.{section}.{subsection}. {title}')
                    continue
        
        # 「章全体のまとめ」「次のステップ」「この章のまとめ」「次章への案内」に節レベルで番号を振る
        if line == '## 章全体のまとめ':
            current_section = 3  # グループ見出しの後の節番号
            current_subsection = 0
            current_subsubsection = 0
            updated_lines.append(f'## 8.{current_section}. 章全体のまとめ')
            continue
        
        if line.startswith('## 次のステップ：'):
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            title = line.replace('## 次のステップ：', '')
            updated_lines.append(f'## 8.{current_section}. 次のステップ：{title}')
            continue
        
        if line == '## この章のまとめ':
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            updated_lines.append(f'## 8.{current_section}. この章のまとめ')
            continue
        
        if line == '## 次章への案内':
            current_section += 1
            current_subsection = 0
            current_subsubsection = 0
            updated_lines.append(f'## 8.{current_section}. 次章への案内')
            continue
        
        # 項レベル（###）の変更（current_section > 0の場合のみ）
        if line.startswith('### ') and current_section > 0:
            current_subsubsection += 1
            
            # 「### 実例：ベトナムで差し歯が取れた（LOG019）」→「#### 8.x.x.x. 実例：ベトナムで差し歯が取れた」
            if line.startswith('### 実例：'):
                # LOG番号を削除
                title = re.sub(r'### 実例：', '', line)
                title = re.sub(r'（LOG\d+）', '', title).strip()
                updated_lines.append(f'#### 8.{current_section}.{current_subsection}.{current_subsubsection}. 実例：{title}')
            # 「### 緊急プロンプト：健康トラブル対処法」
            elif line.startswith('### 緊急プロンプト：'):
                title = re.sub(r'### 緊急プロンプト：', '', line)
                updated_lines.append(f'#### 8.{current_section}.{current_subsection}.{current_subsubsection}. 緊急プロンプト：{title}')
            # 「### 保険請求手続き（LOG051）」
            elif line.startswith('### 保険請求手続き'):
                title = re.sub(r'（LOG\d+）', '', line.replace('### ', '')).strip()
                updated_lines.append(f'#### 8.{current_section}.{current_subsection}.{current_subsubsection}. {title}')
            # 「### 導入部」
            elif line == '### 導入部':
                updated_lines.append(f'#### 8.{current_section}.{current_subsection}.{current_subsubsection}. 導入部')
            # 「### ステップ1：...」
            elif line.startswith('### ステップ'):
                title = line.replace('### ', '')
                updated_lines.append(f'### 8.{current_section}.{current_subsubsection}. {title}')
            # その他の項
            else:
                title = line.replace('### ', '')
                updated_lines.append(f'### 8.{current_section}.{current_subsubsection}. {title}')
            continue
        
        # その他の行はそのまま
        updated_lines.append(line)
    
    # ファイルに書き込み
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))
    
    print(f'第8章の階層番号統一が完了しました: {output_file}')
    print(f'- 節数: {current_section}')

if __name__ == '__main__':
    input_file = '/home/ubuntu/ai_travel_book_project/finals/chapter8_final.md'
    output_file = '/home/ubuntu/ai_travel_book_project/finals/chapter8_final.md'
    update_chapter8_hierarchy(input_file, output_file)
