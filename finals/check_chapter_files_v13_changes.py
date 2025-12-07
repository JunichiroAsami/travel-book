#!/usr/bin/env python3
"""
章ごとのファイルにv13の変更内容が反映されているか確認するスクリプト
"""

import os

def check_chapter_files():
    """章ごとのファイルにv13の変更内容が反映されているか確認"""
    
    print("=" * 80)
    print("章ごとのファイルにv13の変更内容が反映されているか確認")
    print("=" * 80)
    
    # チェック対象ファイル
    files_to_check = {
        'chapter2_final.md': [
            '2.3. 第3部と付録Bの使い分け',
            '第3部（第6章～第9章）：ストーリーの中で学ぶ',
            '付録B：辞書的なリファレンス'
        ],
        'chapter6_final.md': [
            '本章の使い方',
            '本章のプロンプトを今すぐ使いたい方へ'
        ],
        'chapter7_final.md': [
            '本章の使い方',
            '本章のプロンプトを今すぐ使いたい方へ'
        ],
        'chapter8_final.md': [
            '本章の使い方',
            '本章のプロンプトを今すぐ使いたい方へ'
        ],
        'chapter9_final.md': [
            '本章の使い方',
            '本章のプロンプトを今すぐ使いたい方へ'
        ],
        'appendix_b_final.md': [
            '第3部との違い',
            '第3部での詳細解説'
        ]
    }
    
    results = {}
    
    for filename, keywords in files_to_check.items():
        filepath = filename
        
        if not os.path.exists(filepath):
            print(f"\n✗ {filename}: ファイルが見つかりません")
            results[filename] = False
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"\n【{filename}】")
        file_ok = True
        
        for keyword in keywords:
            if keyword in content:
                print(f"  ✓ 「{keyword}」が存在します")
            else:
                print(f"  ✗ 「{keyword}」が見つかりません")
                file_ok = False
        
        results[filename] = file_ok
    
    # 結果サマリー
    print("\n" + "=" * 80)
    print("【結果サマリー】")
    print("=" * 80)
    
    passed = sum(results.values())
    total = len(results)
    
    for filename, ok in results.items():
        status = "✓" if ok else "✗"
        print(f"{status} {filename}")
    
    print(f"\n合格: {passed}/{total} ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n✓ すべての章ごとのファイルにv13の変更内容が反映されています")
    else:
        print(f"\n✗ {total - passed}個のファイルにv13の変更内容が反映されていません")
    
    return results

if __name__ == "__main__":
    check_chapter_files()
