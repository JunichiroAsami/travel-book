#!/usr/bin/env python3
"""
マークダウンファイルの見出しの前に空行を確実に追加するスクリプト
"""

import re

def fix_heading_spacing(input_path, output_path):
    """見出しの前に空行を追加"""
    
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    prev_line_empty = True  # 最初の行の前は空行とみなす
    
    for i, line in enumerate(lines):
        # 見出し行（# で始まる）を検出
        if re.match(r'^#+\s+', line):
            # 前の行が空行でない場合、空行を追加
            if not prev_line_empty:
                fixed_lines.append('\n')
                print(f"行 {i+1}: 見出しの前に空行を追加: {line.strip()[:60]}")
        
        fixed_lines.append(line)
        prev_line_empty = (line.strip() == '')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print(f"\n✓ 修正完了: {output_path}")
    print(f"  - 入力行数: {len(lines)}")
    print(f"  - 出力行数: {len(fixed_lines)}")

if __name__ == "__main__":
    input_path = "complete_manuscript_v16.md"
    output_path = "complete_manuscript_v16_fixed.md"
    
    fix_heading_spacing(input_path, output_path)
