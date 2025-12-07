#!/usr/bin/env python3
"""
参考ログを章末に移動し、番号を統一するスクリプト

第4章以降の形式：
- 本文中：「（LOG014：`ファイル名`より）」
- 注釈：「> **詳細は付録A（WEB限定）のLOG014を参照してください。**」

これを第3章の形式に統一：
- 本文中：「[1]」
- 章末：参考ログセクション
"""

import re
import sys
from pathlib import Path

def extract_log_references(text):
    """
    ログ参照を抽出する
    
    パターン：
    （LOG014：`2025-8-14 15-8-1-_______.md`より）
    
    > **詳細は付録A（WEB限定）のLOG014を参照してください。**
    """
    
    # ログ参照のパターン
    pattern = r'（(LOG[0-9]+)：`([^`]+)`より）\n\n> \*\*詳細は付録A（WEB限定）の\1を参照してください。\*\*'
    
    # すべてのログ参照を抽出
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    
    return matches

def extract_log_info_from_section_title(text):
    """
    セクションタイトルからログ情報を抽出する
    
    パターン：
    ### 実例1：郊外駅の目的地（LOG014）
    """
    
    # セクションタイトルのパターン
    pattern = r'### 実例[0-9]+：(.+)（(LOG[0-9]+)）'
    
    # すべてのセクションタイトルを抽出
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    
    # LOG番号と内容のマッピングを作成
    log_content_map = {}
    for match in matches:
        content = match.group(1)
        log_number = match.group(2)
        log_content_map[log_number] = content
    
    return log_content_map

def standardize_log_references(text):
    """
    ログ参照を標準化する
    """
    
    # ログ参照を抽出
    matches = extract_log_references(text)
    
    if not matches:
        print("  No log references found")
        return text
    
    print(f"  Found {len(matches)} log references")
    
    # セクションタイトルからログ情報を抽出
    log_content_map = extract_log_info_from_section_title(text)
    
    # ログ参照を番号に置き換え、参考ログエントリを作成
    log_entries = []
    reference_number = 1
    
    for match in matches:
        log_number = match.group(1)
        filename = match.group(2)
        
        # 内容を取得
        content = log_content_map.get(log_number, "")
        
        # ログエントリを作成
        log_entries.append({
            'number': f'[{reference_number}]',
            'log_number': log_number,
            'filename': filename,
            'content': content
        })
        
        # 本文中の参照を番号に置き換え
        old_text = match.group(0)
        new_text = f'[{reference_number}]'
        text = text.replace(old_text, new_text, 1)
        
        reference_number += 1
    
    print(f"  Created {len(log_entries)} log entries")
    
    # 参考ログセクションを作成
    reference_section = create_reference_log_section(log_entries)
    
    # まとめセクションの前に挿入
    summary_pattern = r'---\n\n## この章のまとめ'
    
    if re.search(summary_pattern, text):
        text = re.sub(summary_pattern, reference_section + summary_pattern, text, count=1)
        print(f"  Inserted reference log section before summary")
    else:
        # まとめセクションが見つからない場合は、末尾に追加
        text += "\n\n" + reference_section
        print(f"  Appended reference log section at the end")
    
    return text

def create_reference_log_section(log_entries):
    """
    参考ログセクションを作成する
    """
    
    if not log_entries:
        return ""
    
    section = "---\n\n## 参考ログ\n\n"
    section += "| 番号 | ログ番号 | ログファイル名 | 内容 |\n"
    section += "|:---|:---|:---|:---|\n"
    
    for entry in log_entries:
        section += f"| {entry['number']} | {entry['log_number']} | {entry['filename']} | {entry['content']} |\n"
    
    section += "\n"
    
    return section

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 standardize_reference_logs.py <input_file> [output_file]")
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
    
    # ログ参照を標準化
    text = standardize_log_references(text)
    
    # ファイルに書き込む
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Saved: {output_file}")

if __name__ == '__main__':
    main()
