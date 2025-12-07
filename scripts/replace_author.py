#!/usr/bin/env python3
"""
「著者」→「私」の置換スクリプト

注意：
- 「本書の著者」「著者プロフィール」などは置換しない
- 「著者の」「著者は」「著者が」「著者に」「著者を」などは「私の」「私は」「私が」「私に」「私を」に置換
"""

import re
import sys
from pathlib import Path

def replace_author_to_watashi(text):
    """
    「著者」を「私」に置換する
    
    ただし、以下のパターンは置換しない：
    - 「本書の著者」
    - 「著者プロフィール」
    - 「著者について」
    - 「著者名」
    """
    
    # 置換しないパターンをマーク
    text = text.replace('本書の著者', '【KEEP_本書の著者】')
    text = text.replace('著者プロフィール', '【KEEP_著者プロフィール】')
    text = text.replace('著者について', '【KEEP_著者について】')
    text = text.replace('著者名', '【KEEP_著者名】')
    
    # 「著者」を「私」に置換
    text = text.replace('著者', '私')
    
    # マークを元に戻す
    text = text.replace('【KEEP_本書の著者】', '本書の著者')
    text = text.replace('【KEEP_著者プロフィール】', '著者プロフィール')
    text = text.replace('【KEEP_著者について】', '著者について')
    text = text.replace('【KEEP_著者名】', '著者名')
    
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 replace_author.py <input_file> [output_file]")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else input_file
    
    if not input_file.exists():
        print(f"Error: {input_file} does not exist")
        sys.exit(1)
    
    # ファイルを読み込む
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 置換前の「著者」の数を数える
    before_count = text.count('著者')
    
    # 置換
    text = replace_author_to_watashi(text)
    
    # 置換後の「著者」の数を数える
    after_count = text.count('著者')
    
    # ファイルに書き込む
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Replaced: {input_file}")
    print(f"  Before: {before_count} occurrences of '著者'")
    print(f"  After: {after_count} occurrences of '著者'")
    print(f"  Replaced: {before_count - after_count} occurrences")

if __name__ == '__main__':
    main()
