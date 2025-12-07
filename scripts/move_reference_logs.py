#!/usr/bin/env python3
"""
参考ログを章末に移動するスクリプト

各節の末尾にある参考ログを抽出し、章末（まとめの節の前）に移動する。
"""

import re
import sys
from pathlib import Path

def extract_reference_logs(text):
    """
    参考ログセクションを抽出する
    
    パターン：
    ---
    ### 参考ログ
    
    | 番号 | ログファイル名 | 日時 | 内容 |
    |:---|:---|:---|:---|
    | [1] | ... | ... | ... |
    
    > **詳細は付録A（WEB限定）のLOG001を参照してください。**
    
    ---
    """
    
    # 参考ログセクションのパターン
    pattern = r'---\n### 参考ログ\n\n\| 番号 \| ログファイル名 \| 日時 \| 内容 \|\n\|:---\|:---\|:---\|:---\|\n(\| \[[0-9]+\] \| .+ \| .+ \| .+ \|\n)+\n(?:> \*\*詳細は付録A（WEB限定）のLOG[0-9]+を参照してください。\*\*\n\n)?---'
    
    # すべての参考ログセクションを抽出
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    
    return matches

def remove_reference_logs(text):
    """
    参考ログセクションを削除する
    """
    
    # 参考ログセクションのパターン
    pattern = r'---\n### 参考ログ\n\n\| 番号 \| ログファイル名 \| 日時 \| 内容 \|\n\|:---\|:---\|:---\|:---\|\n(\| \[[0-9]+\] \| .+ \| .+ \| .+ \|\n)+\n(?:> \*\*詳細は付録A（WEB限定）のLOG[0-9]+を参照してください。\*\*\n\n)?---'
    
    # すべての参考ログセクションを削除
    text = re.sub(pattern, '', text, flags=re.MULTILINE)
    
    # 連続する空行を削除
    text = re.sub(r'\n\n\n+', '\n\n', text)
    
    return text

def extract_log_entries(matches):
    """
    参考ログのエントリを抽出する
    """
    
    entries = []
    
    for match in matches:
        # マッチしたテキスト
        matched_text = match.group(0)
        
        # ログエントリのパターン
        entry_pattern = r'\| (\[[0-9]+\]) \| (.+) \| (.+) \| (.+) \|'
        
        # すべてのログエントリを抽出
        for entry_match in re.finditer(entry_pattern, matched_text):
            number = entry_match.group(1)
            filename = entry_match.group(2)
            datetime = entry_match.group(3)
            content = entry_match.group(4)
            
            entries.append({
                'number': number,
                'filename': filename,
                'datetime': datetime,
                'content': content
            })
    
    return entries

def create_reference_log_section(entries):
    """
    参考ログセクションを作成する
    """
    
    if not entries:
        return ""
    
    section = "---\n\n## 参考ログ\n\n"
    section += "| 番号 | ログファイル名 | 日時 | 内容 |\n"
    section += "|:---|:---|:---|:---|\n"
    
    for entry in entries:
        section += f"| {entry['number']} | {entry['filename']} | {entry['datetime']} | {entry['content']} |\n"
    
    section += "\n"
    
    return section

def move_reference_logs(text):
    """
    参考ログを章末に移動する
    """
    
    # 参考ログセクションを抽出
    matches = extract_reference_logs(text)
    
    if not matches:
        print("  No reference logs found")
        return text
    
    print(f"  Found {len(matches)} reference log sections")
    
    # ログエントリを抽出
    entries = extract_log_entries(matches)
    
    print(f"  Extracted {len(entries)} log entries")
    
    # 参考ログセクションを削除
    text = remove_reference_logs(text)
    
    # 新しい参考ログセクションを作成
    new_section = create_reference_log_section(entries)
    
    # まとめセクションの前に挿入
    # パターン：「---\n\n## この章のまとめ」
    summary_pattern = r'---\n\n## この章のまとめ'
    
    if re.search(summary_pattern, text):
        text = re.sub(summary_pattern, new_section + summary_pattern, text, count=1)
        print(f"  Inserted reference log section before summary")
    else:
        # まとめセクションが見つからない場合は、末尾に追加
        text += "\n\n" + new_section
        print(f"  Appended reference log section at the end")
    
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 move_reference_logs.py <input_file> [output_file]")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else input_file
    
    if not input_file.exists():
        print(f"Error: {input_file} does not exist")
        sys.exit(1)
    
    # ファイルを読み込む
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f"Processing: {input_file}")
    
    # 参考ログを章末に移動
    text = move_reference_logs(text)
    
    # ファイルに書き込む
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Saved: {output_file}")

if __name__ == '__main__':
    main()
