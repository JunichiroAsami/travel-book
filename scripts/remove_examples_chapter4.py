#!/usr/bin/env python3
"""
第4章から実例4（橋渡り料金、動画レポート）を削除するスクリプト
"""

import re

def remove_examples_from_chapter4(input_file, output_file):
    """第4章から実例4を削除"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 実例4：橋渡り料金について（LOG029）を削除
    pattern1 = r'### 実例4：橋渡り料金について.*?\n\n(?=###)'
    content = re.sub(pattern1, '', content, flags=re.DOTALL)
    
    # 2. 実例4：動画レポート作成（LOG040）を削除
    pattern2 = r'### 実例4：動画レポート作成.*?\n\n(?=###)'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)
    
    # 3. 参考ログの表からLOG029とLOG040を削除
    lines = content.split('\n')
    filtered_lines = []
    
    for line in lines:
        # LOG029またはLOG040を含む行をスキップ
        if 'LOG029' in line or 'LOG040' in line:
            continue
        filtered_lines.append(line)
    
    content = '\n'.join(filtered_lines)
    
    # 4. 参考ログの番号を振り直す（[14]以降を2つずつ減らす）
    # [14] → [14]（変更なし、削除されたため）
    # [15] → [14]
    # [16] → [15]
    # ...
    # [18] → [16]（削除）
    # [19] → [17]
    # [20] → [18]
    
    # まず、削除された[14]と[18]を除いて、番号を振り直す
    # [15] → [14], [16] → [15], [17] → [16], [19] → [17], [20] → [18]
    
    replacements = [
        (r'\[15\]', '[14]'),
        (r'\[16\]', '[15]'),
        (r'\[17\]', '[16]'),
        (r'\[19\]', '[17]'),
        (r'\[20\]', '[18]'),
    ]
    
    for old, new in replacements:
        content = re.sub(old, new, content)
    
    # 5. 出力
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Removed examples from {input_file}")
    print(f"Output saved to {output_file}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python3 remove_examples_chapter4.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    remove_examples_from_chapter4(input_file, output_file)
