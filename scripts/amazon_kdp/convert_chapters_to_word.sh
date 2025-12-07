#!/bin/bash
# 各章のマークダウンファイルをWord形式に変換
# 
# 使用方法:
#   cd /home/ubuntu/ai_travel_book_project/finals
#   chmod +x scripts/convert_chapters_to_word.sh
#   ./scripts/convert_chapters_to_word.sh
#
# 必要なソフトウェア:
#   - Pandoc (バージョン 2.0以降)
#
# 出力:
#   - chapter_00.docx (quickstart.md)
#   - chapter_01.docx (preface.md)
#   - chapter_02.docx (chapter1_final.md)
#   - ...
#   - chapter_16.docx (appendix_c_final.md)

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

# 参照用Word文書
REFERENCE_DOC="complete_manuscript_v10.docx"

# 参照用Word文書の存在確認
if [ ! -f "$REFERENCE_DOC" ]; then
  echo "エラー: 参照用Word文書 '$REFERENCE_DOC' が見つかりません"
  exit 1
fi

echo "========================================="
echo "各章のマークダウンファイルをWord形式に変換"
echo "========================================="
echo ""

# 各ファイルをWord変換
for i in "${!files[@]}"; do
  file="${files[$i]}"
  output="chapter_$(printf "%02d" $i).docx"
  
  # ファイルの存在確認
  if [ ! -f "$file" ]; then
    echo "警告: '$file' が見つかりません。スキップします。"
    continue
  fi
  
  # 最初のファイルのみ目次を付ける
  if [ $i -eq 0 ]; then
    pandoc "$file" -o "$output" \
      --reference-doc="$REFERENCE_DOC" \
      --toc --toc-depth=2 2>&1 | grep -v "WARNING"
  else
    pandoc "$file" -o "$output" \
      --reference-doc="$REFERENCE_DOC" \
      2>&1 | grep -v "WARNING"
  fi
  
  # 変換結果を確認
  if [ -f "$output" ]; then
    echo "✓ $file -> $output"
  else
    echo "✗ $file の変換に失敗しました"
  fi
done

echo ""
echo "========================================="
echo "✓ 全ファイルの変換完了"
echo "========================================="
echo ""
echo "次のステップ:"
echo "  python3.11 scripts/merge_word_files.py"
