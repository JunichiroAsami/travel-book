#!/usr/bin/env python3
"""
章ごとのファイルにv13の変更内容を反映するスクリプト
"""

import re

# 冒頭の案内文
CHAPTER_INTRO = """
**本章の使い方**：本章では、実際の旅行体験を通じて「なぜそのプロンプトを使ったのか」「どう改善したのか」を学べます。プロンプトをすぐに使いたい方は、**付録B**のテンプレート集をご参照ください。

---
"""

# 末尾の対応表
CHAPTER_OUTRO_TEMPLATE = """
---

## 本章のプロンプトを今すぐ使いたい方へ

本章で紹介したプロンプトは、**付録B**でコピペ用テンプレートとして提供しています。以下の対応表から、該当するテンプレートを探してご活用ください。

| 本章のプロンプト | 付録Bの該当テンプレート |
|:---|:---|
| 本章で紹介した各プロンプト | 付録B「1. 旅行計画編」〜「4. 振り返り編」 |

**付録Bの使い方**：
1. 付録Bの目次から、使いたいテンプレートを探す
2. 【】内を自分の情報に置き換える
3. ChatGPTに入力する

---
"""

def update_chapter_file(chapter_num, filename):
    """章ファイルを更新"""
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 第X章の見出しを探す
    chapter_heading = f"# 第{chapter_num}章："
    if chapter_heading not in content:
        print(f"✗ {filename}: 「{chapter_heading}」が見つかりません")
        return False
    
    # 冒頭の案内文を追加（まだ存在しない場合）
    if "**本章の使い方**" not in content:
        # 第X章の見出しの後に案内文を挿入
        content = content.replace(
            chapter_heading,
            chapter_heading + CHAPTER_INTRO,
            1
        )
        print(f"✓ {filename}: 冒頭の案内文を追加しました")
    else:
        print(f"  {filename}: 冒頭の案内文は既に存在します")
    
    # 末尾の対応表を追加（まだ存在しない場合）
    if "## 本章のプロンプトを今すぐ使いたい方へ" not in content:
        # 次章への案内の前に対応表を挿入
        next_chapter_pattern = f"→ \\*\\*第{chapter_num + 1}章"
        if re.search(next_chapter_pattern, content):
            content = re.sub(
                next_chapter_pattern,
                CHAPTER_OUTRO_TEMPLATE + next_chapter_pattern,
                content,
                count=1
            )
            print(f"✓ {filename}: 末尾の対応表を追加しました")
        else:
            # 次章への案内がない場合は、ファイルの末尾に追加
            content += CHAPTER_OUTRO_TEMPLATE
            print(f"✓ {filename}: 末尾の対応表を追加しました（ファイル末尾）")
    else:
        print(f"  {filename}: 末尾の対応表は既に存在します")
    
    # ファイルを保存
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def update_appendix_b():
    """付録Bを更新"""
    
    filename = "appendix_b_final.md"
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 「第3部での詳細解説」を各テンプレートに追加
    template_pattern = r'(### テンプレート\d+：.*?\n\n)'
    
    if "**第3部での詳細解説**" not in content:
        # 各テンプレートの後に「第3部での詳細解説」を追加
        def add_reference(match):
            return match.group(1) + "**第3部での詳細解説**：このプロンプトの背景や使い方の詳細は、第6章〜第9章をご参照ください。\n\n"
        
        content = re.sub(template_pattern, add_reference, content)
        print(f"✓ {filename}: 各テンプレートに「第3部での詳細解説」を追加しました")
        
        # ファイルを保存
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    else:
        print(f"  {filename}: 「第3部での詳細解説」は既に存在します")
        return False

if __name__ == "__main__":
    print("=" * 80)
    print("章ごとのファイルにv13の変更内容を反映")
    print("=" * 80)
    
    # 第6〜9章を更新
    chapters = [
        (6, "chapter6_final.md"),
        (7, "chapter7_final.md"),
        (8, "chapter8_final.md"),
        (9, "chapter9_final.md")
    ]
    
    for chapter_num, filename in chapters:
        print(f"\n【{filename}】")
        update_chapter_file(chapter_num, filename)
    
    # 付録Bを更新
    print(f"\n【appendix_b_final.md】")
    update_appendix_b()
    
    print("\n" + "=" * 80)
    print("✓ 更新完了")
    print("=" * 80)
