# ドキュメント更新サマリー

**更新日**: 2025年12月4日

## 更新内容

### 1. 軽量版参照文書の作成

**ファイル**: `standards/amazon_kdp/reference_document_sample.docx`

- **目的**: Amazon KDP用Word文書作成時の参照文書として使用
- **内容**: v10の最初の2章のみ（823段落）
- **ファイルサイズ**: 142KB（v10の約180KBから削減）
- **スタイル情報**: 完全に保持（ヘッダー、フッター、ページサイズ、余白など）

**作成方法**:
```bash
cd /home/ubuntu/ai_travel_book_project/finals
python3.11 create_reference_sample.py
```

### 2. README.mdの更新

**ファイル**: `/home/ubuntu/ai_travel_book_project/README.md`

**更新箇所**:
- **Word文書の生成プロセス**セクション（65-80行目）
  - 参照用Word文書の前提条件を追加
  - サンプル参照文書の場所を明記

**追加内容**:
```markdown
**前提条件**: 参照用Word文書（`complete_manuscript_v10.docx`）が`finals/`ディレクトリに存在すること
- 参照文書は、Amazon KDP用のフォーマット（ヘッダー、フッター、ページサイズ、余白）を提供します
- サンプル参照文書は`standards/amazon_kdp/reference_document_sample.docx`にあります
```

### 3. Amazon KDP用README.mdの更新

**ファイル**: `standards/amazon_kdp/README.md`

**更新箇所**:

#### 3.1 前提条件セクション（94-101行目）

**更新前**:
```markdown
3. **参照用Word文書** (スタイル定義用)
   - 本書の場合: `complete_manuscript_v10.docx`
```

**更新後**:
```markdown
3. **参照用Word文書** (スタイル定義用)
   - 本プロジェクトに含まれるサンプル: `reference_document_sample.docx`
   - 本書の場合: `complete_manuscript_v10.docx`
   
   **参照文書について**:
   - Pandocの`--reference-doc`オプションで使用
   - ヘッダー、フッター、余白、フォントなどのスタイル情報を提供
   - `reference_document_sample.docx`は最初の2章のみを含む軽量版（スタイル情報は完全に保持）
```

#### 3.2 よくある質問セクション（183-185行目）

**更新前**:
```markdown
### Q2: 参照用Word文書（complete_manuscript_v10.docx）は必須ですか？

**A**: 必須ではありませんが、スタイルの一貫性を保つために強く推奨します。参照用Word文書がない場合、Pandocはデフォルトのスタイルを使用します。
```

**更新後**:
```markdown
### Q2: 参照用Word文書は必須ですか？

**A**: **必須**です。Amazon KDP用の正しいフォーマット（ヘッダー、フッター、ページサイズ、余白など）を適用するために必要です。本プロジェクトには`reference_document_sample.docx`が含まれています。これは最初の2章のみを含む軽量版ですが、スタイル情報は完全に保持されています。
```

#### 3.3 ファイル構成セクション（140-189行目）

**更新内容**:
- プロジェクト全体の構成を反映
- `reference_document_sample.docx`を追加
- 参照文書の説明を追加

```markdown
**参照文書について**:
- `reference_document_sample.docx`: 軽量版（最初の2章のみ、約142KB）
- `complete_manuscript_v10.docx`: フル版（全17章、約180KB）
- どちらもスタイル情報は同じ（ヘッダー、フッター、ページサイズ、余白など）
- Pandocの`--reference-doc`オプションで使用可能
```

## 更新の理由

### 問題点
- v19のサンプルを渡さないと正しいフォーマットのWord文書が作成できないのではないか？
- 参照文書の重要性が明確に説明されていない

### 解決策
1. **軽量版参照文書を作成**
   - プロジェクトに含めることで、誰でも正しいフォーマットのWord文書を作成可能
   - ファイルサイズを削減（最初の2章のみ）
   - スタイル情報は完全に保持

2. **ドキュメントを更新**
   - 参照文書の重要性を明記（「必須」と強調）
   - 参照文書の役割を説明（ヘッダー、フッター、ページサイズ、余白など）
   - サンプル参照文書の場所を明示

## 今後の使用方法

### 新しいプロジェクトで使用する場合

1. `standards/amazon_kdp/reference_document_sample.docx`をコピー
2. `finals/`ディレクトリに配置（または`convert_chapters_to_word.sh`の`REFERENCE_DOC`変数を更新）
3. 通常のプロセスでWord文書を作成

### 既存のプロジェクトで使用する場合

1. 既にv10などの参照文書がある場合はそのまま使用可能
2. 参照文書がない場合は、`reference_document_sample.docx`をコピー

## 検証

### 参照文書サンプルの検証

```bash
cd /home/ubuntu/ai_travel_book_project/finals
python3.11 << 'EOF'
from docx import Document

doc = Document("../standards/amazon_kdp/reference_document_sample.docx")

print("【参照文書サンプルの情報】")
print(f"  段落数: {len(doc.paragraphs):,}")
print(f"  セクション数: {len(doc.sections)}")

section = doc.sections[0]
print(f"  ページサイズ: {section.page_width.cm:.2f}cm × {section.page_height.cm:.2f}cm")
print(f"  余白: 上{section.top_margin.cm:.2f}cm、下{section.bottom_margin.cm:.2f}cm、左{section.left_margin.cm:.2f}cm、右{section.right_margin.cm:.2f}cm")

heading1_count = sum(1 for para in doc.paragraphs if para.style.name == 'Heading 1')
print(f"  見出し1の数: {heading1_count}")
EOF
```

**期待される出力**:
```
【参照文書サンプルの情報】
  段落数: 823
  セクション数: 1
  ページサイズ: 15.44cm × 21.64cm
  余白: 上1.27cm、下1.27cm、左1.27cm、右1.27cm
  見出し1の数: 2
```

## まとめ

今回の更新により、以下が実現されました:

1. ✅ **参照文書の重要性を明確化**（「必須」と強調）
2. ✅ **軽量版参照文書を提供**（プロジェクトに含める）
3. ✅ **ドキュメントを更新**（使用方法を明記）
4. ✅ **再現性の向上**（誰でも正しいフォーマットのWord文書を作成可能）

これにより、v19のサンプルを渡さなくても、`reference_document_sample.docx`を使用することで、正しいフォーマットのAmazon KDP用Word文書を作成できるようになりました。
