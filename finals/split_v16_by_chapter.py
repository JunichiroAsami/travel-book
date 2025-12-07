#!/usr/bin/env python3
"""
v16を章ごとに分割するスクリプト
"""

import re

def split_by_chapter(input_path, output_dir="."):
    """マークダウンファイルを章ごとに分割"""
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Heading 1で分割（# で始まる行）
    # ただし、## や ### は除外
    pattern = r'^# [^#].*$'
    matches = list(re.finditer(pattern, content, re.MULTILINE))
    
    print(f"検出されたHeading 1: {len(matches)}個")
    
    chapters = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        
        chapter_content = content[start:end]
        chapter_title = match.group().strip()
        
        # ファイル名を生成
        if "クイックスタート" in chapter_title:
            filename = f"{output_dir}/v16_part_00_quickstart.md"
        elif "はじめに" in chapter_title:
            filename = f"{output_dir}/v16_part_01_preface.md"
        elif "第1章" in chapter_title:
            filename = f"{output_dir}/v16_part_02_chapter01.md"
        elif "第2章" in chapter_title:
            filename = f"{output_dir}/v16_part_03_chapter02.md"
        elif "第3章" in chapter_title:
            filename = f"{output_dir}/v16_part_04_chapter03.md"
        elif "第4章" in chapter_title:
            filename = f"{output_dir}/v16_part_05_chapter04.md"
        elif "第5章" in chapter_title:
            filename = f"{output_dir}/v16_part_06_chapter05.md"
        elif "第6章" in chapter_title:
            filename = f"{output_dir}/v16_part_07_chapter06.md"
        elif "第7章" in chapter_title:
            filename = f"{output_dir}/v16_part_08_chapter07.md"
        elif "第8章" in chapter_title:
            filename = f"{output_dir}/v16_part_09_chapter08.md"
        elif "第9章" in chapter_title:
            filename = f"{output_dir}/v16_part_10_chapter09.md"
        elif "第10章" in chapter_title:
            filename = f"{output_dir}/v16_part_11_chapter10.md"
        elif "第11章" in chapter_title:
            filename = f"{output_dir}/v16_part_12_chapter11.md"
        elif "第12章" in chapter_title:
            filename = f"{output_dir}/v16_part_13_chapter12.md"
        elif "おわりに" in chapter_title:
            filename = f"{output_dir}/v16_part_14_afterword.md"
        elif "付録B" in chapter_title:
            filename = f"{output_dir}/v16_part_15_appendix_b.md"
        elif "ハノイ" in chapter_title:
            filename = f"{output_dir}/v16_part_16_hanoi.md"
        elif "付録C" in chapter_title:
            filename = f"{output_dir}/v16_part_17_appendix_c.md"
        else:
            filename = f"{output_dir}/v16_part_{i:02d}_unknown.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(chapter_content)
        
        print(f"{i+1:2}. {chapter_title[:60]:60} -> {filename}")
        chapters.append((chapter_title, filename))
    
    return chapters

if __name__ == "__main__":
    input_path = "complete_manuscript_v16_fixed.md"
    chapters = split_by_chapter(input_path)
    print(f"\n✓ 分割完了: {len(chapters)}個のファイル")
