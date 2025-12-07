#!/usr/bin/env python3
"""
v13の構造を修正するスクリプト
- 重複した「はじめに」を1つに統合
- 重複した「おわりに」を1つに統合
- 「今すぐ使える！AIプロンプト9選」を「クイックスタートガイド」に変更
- 「免責事項」と「ハノイ3日間の旅」のHeading 1を Heading 2に変更
"""

def fix_v13_structure(input_path, output_path):
    """v13の構造を修正"""
    
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    skip_next_preface = False
    skip_next_afterword = False
    preface_count = 0
    afterword_count = 0
    
    for i, line in enumerate(lines):
        # 「はじめに」の処理
        if line.strip() == '# はじめに':
            preface_count += 1
            if preface_count == 1:
                # 1つ目の「はじめに」はスキップ（空のセクション）
                skip_next_preface = True
                print(f"行 {i+1}: 1つ目の「はじめに」をスキップ")
                continue
            elif preface_count == 2:
                # 2つ目の「はじめに」を残す
                fixed_lines.append(line)
                print(f"行 {i+1}: 2つ目の「はじめに」を残す")
                continue
        
        # 「今すぐ使える！AIプロンプト9選」を「クイックスタートガイド」に変更
        if line.strip() == '# 今すぐ使える！AIプロンプト9選':
            fixed_lines.append('# クイックスタートガイド\n')
            print(f"行 {i+1}: 「今すぐ使える！AIプロンプト9選」→「クイックスタートガイド」")
            continue
        
        # 「おわりに」の処理
        if line.strip() == '# おわりに':
            afterword_count += 1
            if afterword_count == 1:
                # 1つ目の「おわりに」を残す
                fixed_lines.append(line)
                print(f"行 {i+1}: 1つ目の「おわりに」を残す")
                continue
            elif afterword_count == 2:
                # 2つ目の「おわりに」をスキップ
                skip_next_afterword = True
                print(f"行 {i+1}: 2つ目の「おわりに」をスキップ")
                continue
        
        # 「免責事項」のHeading 1をHeading 2に変更
        if line.strip() == '# 免責事項（ディスクレーマー）':
            fixed_lines.append('## 免責事項（ディスクレーマー）\n')
            print(f"行 {i+1}: 「免責事項」をHeading 2に変更")
            continue
        
        # 「ハノイ3日間の旅」のHeading 1をHeading 2に変更
        if line.strip().startswith('# ハノイ3日間の旅'):
            fixed_lines.append('## ' + line.strip()[2:] + '\n')
            print(f"行 {i+1}: 「ハノイ3日間の旅」をHeading 2に変更")
            continue
        
        fixed_lines.append(line)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print(f"\n✓ 修正完了: {output_path}")
    print(f"  - 入力行数: {len(lines)}")
    print(f"  - 出力行数: {len(fixed_lines)}")

if __name__ == "__main__":
    input_path = "complete_manuscript_v13.md"
    output_path = "complete_manuscript_v13_corrected.md"
    
    fix_v13_structure(input_path, output_path)
