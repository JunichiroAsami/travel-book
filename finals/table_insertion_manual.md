# Pandocのテーブル認識問題を回避し、Word文書に手動でテーブルを挿入する方法

## 1. はじめに

`pandoc`を使用してMarkdownからWord(.docx)へ変換する際、特定の条件下でパイプテーブルが正しく認識されない問題が発生します。本ドキュメントでは、この問題を回避し、`python-docx`ライブラリを使って手動でテーブルを挿入する手順を解説します。

## 2. 問題の概要

- **現象**: Markdownファイル内の一部のパイプテーブルが、`pandoc`によるWord変換時に無視される。
- **原因**: `pandoc`のパーサーが、特定のヘッダー階層やリスト構造の後に続くテーブルを正しく解釈できない場合がある。

## 3. 解決策の概要

この問題は、以下の3ステップのアプローチで解決できます。

1.  **プレースホルダーの設置**: Markdownファイル内のテーブルを、一意のテキストプレースホルダー（例: `【テーブル挿入位置】`）に置き換える。
2.  **Pandocによる変換**: プレースホルダーを含むMarkdownファイルを通常通り`pandoc`でWord文書に変換する。
3.  **Pythonスクリプトによるテーブル挿入**: `python-docx`を使い、変換後のWord文書内のプレースホルダーを検索し、その位置にプログラムでテーブルを生成・挿入する。

## 4. 詳細な手順

### ステップ1: Markdownファイルの準備

`pandoc`で認識されないテーブルをMarkdownファイルから削除し、その場所にプレースホルダーテキストを挿入します。

**変更前 (例: `chapter3_final.md`)**

```markdown
...ホテル詳細説明...

| ホテル名 | 予算 | 朝食 | プール | ルーフトップバー | トゥクトゥク乗車 |
|:---|:---|:---|:---|:---|:---|
| Avani+ Riverside | ◎ 約1万円台 | ◎ 豊富＋景観 | ◎ インフィニティプール | ◎ プール併設バー | ○ 川沿い移動可 |
| ... | ... | ... | ... | ... | ... |

トゥクトゥクも楽しみたい方へ
...
```

**変更後 (例: `chapter3_no_table.md`)**

```markdown
...ホテル詳細説明...

【テーブル挿入位置】

トゥクトゥクも楽しみたい方へ
...
```

### ステップ2: PandocによるWord文書への変換

ターミナルで以下のコマンドを実行し、変更後のMarkdownファイルをWord文書に変換します。

```bash
pandoc chapter3_no_table.md -o chapter3_with_placeholder.docx
```

### ステップ3: `python-docx`によるテーブルの挿入

以下のPythonスクリプトを実行して、プレースホルダーの位置にテーブルを挿入します。このスクリプトは、文書内の全段落をスキャンし、プレースホルダーテキストを含む段落を見つけ、その段落を削除した上で、同じ位置に新しいテーブルを挿入します。

**Pythonスクリプト (`insert_table.py`)**

```python
from docx import Document
from docx.shared import Pt

# --- 設定 ---
docx_path = 'chapter3_with_placeholder.docx' # 入力ファイル
output_path = 'chapter3_final_complete.docx' # 出力ファイル
placeholder_text = '【テーブル挿入位置】'

# --- テーブルデータ ---
table_data = [
    ['ホテル名', '予算', '朝食', 'プール', 'ルーフトップバー', 'トゥクトゥク乗車'],
    ['Avani+ Riverside', '◎ 約1万円台', '◎ 豊富＋景観', '◎ インフィニティプール', '◎ プール併設バー', '○ 川沿い移動可'],
    ['Eastin Grand Sathorn', '◎ リーズナブル', '◎ フルーツ・オムレツ', '◎ 屋外プール', '○ 屋外バーあり', '○ 近隣で利用可'],
    ['Marriott Surawongse', '○ 3万円前後', '○ 多国籍ビュッフェ', '◎ インフィニティプール', '◎ 360°景観', '○ シーロム界隈'],
    ['Sivatel バンコク', '◎ 約2,500THB～', '○ 種類少なめ', '○ 屋外プール', '× 明記なし', '○ 近隣で利用可']
]

# --- 処理 ---
doc = Document(docx_path)

for p in doc.paragraphs:
    if placeholder_text in p.text:
        # プレースホルダーの段落を特定
        target_paragraph = p
        print(f"プレースホルダー '{placeholder_text}' を段落内で見つけました。")

        # テーブルを作成
        table = doc.add_table(rows=len(table_data), cols=len(table_data[0]))
        table.autofit = True # 自動フィットを有効にする

        # テーブルにデータを入力
        for i, row_data in enumerate(table_data):
            for j, cell_data in enumerate(row_data):
                cell = table.rows[i].cells[j]
                cell.text = cell_data
                # フォントサイズなどを設定
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.size = Pt(10)

        # プレースホルダーの段落をテーブルに置き換える
        # プレースホルダーの段落の親要素を取得
        parent = target_paragraph._p.getparent()
        # プレースホルダーの段落の前にテーブルを挿入
        parent.insert(parent.index(target_paragraph._p), table._element)
        # プレースホルダーの段落を削除
        parent.remove(target_paragraph._p)

        print("テーブルの挿入とプレースホルダーの削除が完了しました。")
        break # 最初のプレースホルダーのみ処理

# 文書を保存
doc.save(output_path)
print(f"処理済みのファイルを '{output_path}' として保存しました。")

```

## 5. 結論

この「プレースホルダーとスクリプト」方式により、`pandoc`の制限に左右されることなく、意図した通りの位置と内容でテーブルを確実にWord文書に含めることができます。原稿全体の自動化処理にも応用可能です。
