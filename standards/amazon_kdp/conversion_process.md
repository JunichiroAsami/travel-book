# マークダウンからAmazon KDP用Word文書への変換プロセス

**最終更新日**: 2025年12月4日

## 概要

このドキュメントでは、章ごとのマークダウンファイルからAmazon KDP用Word文書を作成するプロセスを詳細に説明します。

## 前提条件

### 必要なソフトウェア

1. **Pandoc** (バージョン 2.0以降)
   ```bash
   pandoc --version
   ```

2. **Python 3.11** (python-docxライブラリ)
   ```bash
   python3.11 --version
   pip3 install python-docx
   ```

3. **参照用Word文書** (スタイル定義用)
   - 本書の場合: `complete_manuscript_v10.docx`

### ファイル構成の確認

以下のファイルが存在することを確認してください：

```
/home/ubuntu/ai_travel_book_project/finals/
├── quickstart.md
├── preface.md
├── chapter1_final.md
├── chapter2_final.md
├── chapter3_final.md
├── chapter4_final.md
├── chapter5_final.md
├── chapter6_final.md
├── chapter7_final.md
├── chapter8_final.md
├── chapter9_final.md
├── chapter10_final.md
├── chapter11_final.md
├── chapter12_final.md
├── afterword.md
├── appendix_b_final.md
├── appendix_c_final.md
└── complete_manuscript_v10.docx  # 参照用
```

## プロセス全体の流れ

```
┌─────────────────────────────────────┐
│ 1. 章ごとのマークダウンファイル    │
│    (quickstart.md, chapter1_final.md, etc.) │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│ 2. 各章を個別にPandocでWord変換     │
│    (chapter_00.docx, chapter_01.docx, etc.) │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│ 3. python-docxで17個のWordファイルを結合 │
│    (complete_manuscript_v18_final.docx)    │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│ 4. 目次の更新とページ番号の設定     │
│    (手動でWordで実施)                │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│ 5. Amazon KDPに提出                 │
└─────────────────────────────────────┘
```

## ステップ1: 各章を個別にPandocでWord変換

### 1.1. 変換スクリプトの作成

`convert_chapters_to_word.sh`を作成します：

```bash
#!/bin/bash
# 各章のマークダウンファイルをWord形式に変換

# 作業ディレクトリに移動
cd /home/ubuntu/ai_travel_book_project/finals

# 各章のファイルリスト
files=(
  "quickstart.md"
  "preface.md"
  "chapter1_final.md"
  "chapter2_final.md"
  "chapter3_final.md"
  "chapter4_final.md"
  "chapter5_final.md"
  "chapter6_final.md"
  "chapter7_final.md"
  "chapter8_final.md"
  "chapter9_final.md"
  "chapter10_final.md"
  "chapter11_final.md"
  "chapter12_final.md"
  "afterword.md"
  "appendix_b_final.md"
  "appendix_c_final.md"
)

# 各ファイルをWord変換
for i in "${!files[@]}"; do
  file="${files[$i]}"
  output="chapter_$(printf "%02d" $i).docx"
  
  # 最初のファイルのみ目次を付ける
  if [ $i -eq 0 ]; then
    pandoc "$file" -o "$output" \
      --reference-doc=complete_manuscript_v10.docx \
      --toc --toc-depth=2 2>&1 | grep -v "WARNING"
  else
    pandoc "$file" -o "$output" \
      --reference-doc=complete_manuscript_v10.docx \
      2>&1 | grep -v "WARNING"
  fi
  
  echo "✓ $file -> $output"
done

echo "✓ 全ファイルの変換完了"
```

### 1.2. スクリプトの実行

```bash
cd /home/ubuntu/ai_travel_book_project/finals
chmod +x convert_chapters_to_word.sh
./convert_chapters_to_word.sh
```

### 1.3. Pandocのオプション説明

| オプション | 説明 |
|:---|:---|
| `--reference-doc=complete_manuscript_v10.docx` | 参照用Word文書（スタイル定義を継承） |
| `--toc` | 目次を自動生成 |
| `--toc-depth=2` | 目次の深さをHeading 2まで |
| `2>&1 \| grep -v "WARNING"` | 警告メッセージを非表示 |

## ステップ2: 17個のWordファイルを結合

### 2.1. 結合スクリプトの作成

`merge_word_files.py`を作成します：

```python
#!/usr/bin/env python3
"""
17個のWordファイルを結合してAmazon KDP用の完成版を作成
"""

from docx import Document

def merge_word_files():
    """17個のWordファイルを結合"""
    
    # 最初のファイルを読み込み（目次付き）
    doc = Document('chapter_00.docx')
    print(f'✓ chapter_00.docx を読み込みました')
    
    # 残りのファイルを順番に追加
    for i in range(1, 17):
        chapter_file = f'chapter_{i:02d}.docx'
        chapter_doc = Document(chapter_file)
        
        # 章の内容を追加
        for element in chapter_doc.element.body:
            doc.element.body.append(element)
        
        print(f'✓ {chapter_file} を追加しました')
    
    # 保存
    output_file = 'complete_manuscript_v18_final.docx'
    doc.save(output_file)
    print(f'\n✓ 結合完了: {output_file}')
    
    # 確認
    heading1_list = [p.text for p in doc.paragraphs if p.style.name == 'Heading 1']
    print(f'\nHeading 1の数: {len(heading1_list)}')
    
    if len(heading1_list) == 17:
        print('✓ すべてのHeading 1が存在します')
    else:
        print(f'✗ Heading 1が{len(heading1_list)}個です（期待値: 17）')

if __name__ == "__main__":
    merge_word_files()
```

### 2.2. スクリプトの実行

```bash
cd /home/ubuntu/ai_travel_book_project/finals
python3.11 merge_word_files.py
```

### 2.3. 結合の仕組み

python-docxの`element.body.append()`を使用して、各章のWord文書の内容を順番に結合します。

```python
# 章の内容を追加
for element in chapter_doc.element.body:
    doc.element.body.append(element)
```

この方法により、各章のフォーマット、スタイル、画像、表などがそのまま保持されます。

## ステップ3: 目次の更新とページ番号の設定

### 3.1. 目次の更新

1. `complete_manuscript_v18_final.docx`をWordで開く
2. 目次を右クリック
3. 「フィールドの更新」を選択
4. 「目次をすべて更新する」を選択
5. 「OK」をクリック

### 3.2. ページ番号の設定

1. ページ番号をダブルクリック（ヘッダー/フッター編集モードに入る）
2. 「ページ番号」→「ページ番号の書式設定」を選択
3. 「開始番号」を「1」に設定
4. 「OK」をクリック
5. ヘッダー/フッター編集モードを終了

## ステップ4: 検証

### 4.1. 見出し構造の確認

`verify_word_structure.py`を使用して、Word文書の見出し構造を確認します：

```python
#!/usr/bin/env python3
"""
Word文書の見出し構造を確認
"""

from docx import Document

def verify_word_structure(docx_file):
    """Word文書の見出し構造を確認"""
    
    doc = Document(docx_file)
    
    heading1_list = []
    heading1_count = 0
    heading2_count = 0
    heading3_count = 0
    
    for para in doc.paragraphs:
        if para.style.name == 'Heading 1':
            heading1_list.append(para.text)
            heading1_count += 1
        elif para.style.name == 'Heading 2':
            heading2_count += 1
        elif para.style.name == 'Heading 3':
            heading3_count += 1
    
    print(f'Word文書の見出し構造: {docx_file}')
    print('=' * 80)
    print(f'段落数: {len(doc.paragraphs):,}')
    print(f'Heading 1: {heading1_count}')
    print(f'Heading 2: {heading2_count}')
    print(f'Heading 3: {heading3_count}')
    print('\nHeading 1の一覧:')
    print('-' * 80)
    for i, title in enumerate(heading1_list, start=1):
        print(f'{i:2}. {title}')
    print('-' * 80)
    print(f'期待されるHeading 1: 17')
    print(f'実際のHeading 1: {heading1_count}')
    
    if heading1_count == 17:
        print('✓ すべてのHeading 1が存在します')
    else:
        print(f'✗ {abs(17 - heading1_count)}個のHeading 1が{"不足" if heading1_count < 17 else "超過"}しています')

if __name__ == "__main__":
    verify_word_structure('complete_manuscript_v18_final.docx')
```

実行：

```bash
python3.11 verify_word_structure.py
```

### 4.2. 内容の確認

以下の項目を確認します：

- [ ] Heading 1が17個存在する
- [ ] 目次が正しく生成されている
- [ ] ページ番号が正しく設定されている
- [ ] 各章の内容が正しく表示されている
- [ ] 画像が正しく表示されている
- [ ] 表が正しく表示されている
- [ ] リンクが正しく機能している

## ステップ5: Amazon KDPに提出

### 5.1. 最終チェック

1. ファイルサイズを確認（50MB以下）
2. ファイル形式を確認（.docx）
3. ファイル名を確認（わかりやすい名前に変更）

### 5.2. 提出

1. [Amazon KDP](https://kdp.amazon.co.jp/)にログイン
2. 「新しい本を作成」をクリック
3. 「Kindle本の詳細」を入力
4. 「Kindle本のコンテンツ」で`complete_manuscript_v18_final.docx`をアップロード
5. プレビューを確認
6. 「保存して続行」をクリック

## トラブルシューティング

### 問題1: Pandocが一部の見出しを認識しない

**症状**: 大きなマークダウンファイルを変換すると、一部の見出しがHeading 1として認識されない

**解決策**: 章ごとに個別変換してから結合する（本プロセスで採用）

### 問題2: 「第3部：実践編」がHeading 1として認識される

**症状**: chapter6_final.mdの「# 第3部：実践編」がHeading 1として認識される

**解決策**: `# 第3部：実践編`を`## 第3部：実践編`に変更

### 問題3: python-docxでの結合時にフォーマットが崩れる

**症状**: 結合後のWord文書でフォーマットが崩れる

**解決策**: すべての章で同じ参照用Word文書（`complete_manuscript_v10.docx`）を使用する

## まとめ

このプロセスにより、章ごとのマークダウンファイルから、Amazon KDP用のWord文書を確実に作成できます。

**重要なポイント**:
1. 章ごとに個別変換することで、Pandocの制限を回避
2. python-docxで結合することで、フォーマットを保持
3. 参照用Word文書を使用することで、スタイルを統一

## 参考資料

- [Pandoc User's Guide](https://pandoc.org/MANUAL.html)
- [python-docx Documentation](https://python-docx.readthedocs.io/)
- [Amazon KDP ヘルプ](https://kdp.amazon.co.jp/ja_JP/help)
