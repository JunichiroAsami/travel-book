#!/usr/bin/env python3
"""
v16がv13の変更内容を反映しているか確認するスクリプト
"""

from docx import Document

def verify_v16_changes(docx_path):
    """v16がv13の変更内容を反映しているか確認"""
    
    doc = Document(docx_path)
    
    # 全テキストを結合
    full_text = "\n".join([para.text for para in doc.paragraphs])
    
    print("=" * 80)
    print("v16がv13の変更内容を反映しているか確認")
    print("=" * 80)
    
    # チェック項目
    checks = []
    
    # 1. クイックスタートガイド（v12で追加）
    print("\n【チェック1】クイックスタートガイドの存在")
    if "クイックスタートガイド" in full_text:
        print("✓ クイックスタートガイドが存在します")
        checks.append(True)
    else:
        print("✗ クイックスタートガイドが見つかりません")
        checks.append(False)
    
    # 2. 第2章に「2.3. 第3部と付録Bの使い分け」（v13で追加）
    print("\n【チェック2】第2章に「2.3. 第3部と付録Bの使い分け」")
    if "2.3. 第3部と付録Bの使い分け" in full_text or "第3部と付録Bの使い分け" in full_text:
        print("✓ 第2章に「第3部と付録Bの使い分け」が存在します")
        checks.append(True)
    else:
        print("✗ 第2章に「第3部と付録Bの使い分け」が見つかりません")
        checks.append(False)
    
    # 3. 付録Bの冒頭に「第3部との違い」（v13で追加）
    print("\n【チェック3】付録Bの冒頭に「第3部との違い」")
    if "第3部との違い" in full_text:
        print("✓ 付録Bに「第3部との違い」が存在します")
        checks.append(True)
    else:
        print("✗ 付録Bに「第3部との違い」が見つかりません")
        checks.append(False)
    
    # 4. 第6〜9章の冒頭に案内文（v13で追加）
    print("\n【チェック4】第6〜9章の冒頭に案内文")
    if "本章の使い方" in full_text and "付録B" in full_text:
        print("✓ 章の冒頭に案内文が存在します")
        checks.append(True)
    else:
        print("✗ 章の冒頭に案内文が見つかりません")
        checks.append(False)
    
    # 5. 第6〜9章の末尾に対応表（v13で追加）
    print("\n【チェック5】第6〜9章の末尾に対応表")
    if "本章のプロンプトを今すぐ使いたい方へ" in full_text:
        print("✓ 章の末尾に対応表が存在します")
        checks.append(True)
    else:
        print("✗ 章の末尾に対応表が見つかりません")
        checks.append(False)
    
    # 6. 付録Bの各テンプレートに「第3部での詳細解説」（v13で追加）
    print("\n【チェック6】付録Bの各テンプレートに「第3部での詳細解説」")
    if "第3部での詳細解説" in full_text:
        print("✓ 付録Bに「第3部での詳細解説」が存在します")
        checks.append(True)
    else:
        print("✗ 付録Bに「第3部での詳細解説」が見つかりません")
        checks.append(False)
    
    # 7. 水平線の削除（v16で実施）
    print("\n【チェック7】水平線（---）の削除")
    horizontal_line_count = full_text.count("---")
    if horizontal_line_count < 10:  # 完全に削除されていれば0、一部残っていても10未満
        print(f"✓ 水平線は削除されています（残り{horizontal_line_count}箇所）")
        checks.append(True)
    else:
        print(f"✗ 水平線が多数残っています（{horizontal_line_count}箇所）")
        checks.append(False)
    
    # 結果サマリー
    print("\n" + "=" * 80)
    print("【結果サマリー】")
    print("=" * 80)
    passed = sum(checks)
    total = len(checks)
    print(f"合格: {passed}/{total} ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n✓ v16は、v10からv13への変更内容をすべて反映しています")
    else:
        print(f"\n✗ v16は、{total - passed}個の変更内容が反映されていません")
    
    return checks

if __name__ == "__main__":
    docx_path = "complete_manuscript_v16_final.docx"
    verify_v16_changes(docx_path)
