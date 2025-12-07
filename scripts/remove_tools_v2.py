#!/usr/bin/env python3
"""
付録Cから特定のツール（Papago、Otter.ai、Whisper、Notta）を完全に削除するスクリプト v2
"""

import re

def remove_tools_completely(input_file, output_file):
    """付録Cから特定ツールを完全に削除"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 削除対象のツール
    tools = ['Papago', 'Otter.ai', 'Whisper', 'Notta']
    
    result_lines = []
    skip_until_next_section = False
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # ステップセクションで削除対象ツールが含まれている場合、次のステップまでスキップ
        if re.match(r'\*\*ステップ\d+:', line):
            contains_tool = any(tool in line for tool in tools)
            if contains_tool:
                # 次のステップまたはセクションまでスキップ
                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    if re.match(r'\*\*ステップ\d+:', next_line) or re.match(r'^\*\*.*\*\*:', next_line) or next_line.startswith('##'):
                        break
                    i += 1
                continue
        
        # 削除対象ツールを含む行をスキップ
        if any(tool in line for tool in tools):
            # ただし、見出しや重要な構造は保持
            if not (line.startswith('#') or line.startswith('|:---')):
                i += 1
                continue
        
        result_lines.append(line)
        i += 1
    
    # 空行を整理
    final_lines = []
    empty_count = 0
    
    for line in result_lines:
        if line.strip() == '':
            empty_count += 1
            if empty_count <= 2:
                final_lines.append(line)
        else:
            empty_count = 0
            final_lines.append(line)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    
    print(f"Completely removed tools from {input_file}")
    print(f"Output saved to {output_file}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python3 remove_tools_v2.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    remove_tools_completely(input_file, output_file)
