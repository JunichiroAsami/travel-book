#!/usr/bin/env python3
"""
付録Cから特定のツール（Papago、Otter.ai、Whisper、Notta）を削除するスクリプト
"""

import re

def remove_tools_from_appendix_c(input_file, output_file):
    """付録Cから特定ツールを削除"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 削除対象のツール
    tools_to_remove = ['Papago', 'Otter.ai', 'Whisper', 'Notta']
    
    # 1. 各ツールの専用セクションを削除（#### 見出しから次の見出しまで）
    for tool in tools_to_remove:
        # #### ツール名（...） から次の #### または ### まで削除
        pattern = rf'#### {re.escape(tool)}.*?\n\n(.*?)(?=\n###|\n####|\Z)'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # 2. ツール一覧表から該当行を削除
    lines = content.split('\n')
    filtered_lines = []
    
    for line in lines:
        # 表の行で、削除対象ツールが含まれている場合はスキップ
        if '|' in line:
            should_skip = False
            for tool in tools_to_remove:
                if tool in line and not line.startswith('|:---'):
                    should_skip = True
                    break
            if should_skip:
                continue
        
        filtered_lines.append(line)
    
    content = '\n'.join(filtered_lines)
    
    # 3. 本文中の言及を削除
    # 「現地ガイドの説明を自動で文字起こししたい時 → Otter.ai」のような行を削除
    for tool in tools_to_remove:
        pattern = rf'^- \*\*.*?\*\* → {re.escape(tool)}.*?$'
        content = re.sub(pattern, '', content, flags=re.MULTILINE)
    
    # 4. リストからツール名を削除
    for tool in tools_to_remove:
        # - **Otter.ai**: ... のような行を削除
        pattern = rf'^- \*\*{re.escape(tool)}\*\*:.*?$'
        content = re.sub(pattern, '', content, flags=re.MULTILINE)
        
        # - Otter.ai → ... のような行を削除
        pattern = rf'^- {re.escape(tool)} →.*?$'
        content = re.sub(pattern, '', content, flags=re.MULTILINE)
    
    # 5. 文中の言及を削除（例：「Otter.aiで記録」→削除）
    # ステップタイトルを削除
    for tool in tools_to_remove:
        pattern = rf'\*\*ステップ\d+: {re.escape(tool)}.*?\*\*'
        content = re.sub(pattern, '', content)
    
    # 6. 複数ツールのリスト（例：「DeepL、Papago、Microsoft翻訳」）からツール名を削除
    for tool in tools_to_remove:
        # カンマ区切りリストから削除
        content = re.sub(rf'、{re.escape(tool)}', '', content)
        content = re.sub(rf'{re.escape(tool)}、', '', content)
    
    # 7. 空行を整理（3行以上の連続した空行を2行に）
    content = re.sub(r'\n\n\n+', '\n\n', content)
    
    # 8. 出力
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Removed tools from {input_file}")
    print(f"Output saved to {output_file}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python3 remove_tools_from_appendix_c.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    remove_tools_from_appendix_c(input_file, output_file)
