#!/bin/bash
# 章ごとのマークダウンファイルを結合して統合マークダウンファイルを作成
#
# 使用方法:
#   cd /home/ubuntu/ai_travel_book_project/finals
#   chmod +x scripts/create_combined_markdown.sh
#   ./scripts/create_combined_markdown.sh
#
# 出力:
#   - complete_manuscript_v18.md

# 作業ディレクトリに移動
cd /home/ubuntu/ai_travel_book_project/finals

# 出力ファイル名
OUTPUT_FILE="complete_manuscript_v18.md"

echo "========================================="
echo "章ごとのマークダウンファイルを結合"
echo "========================================="
echo ""

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

# ファイルの存在確認
missing_files=()
for file in "${files[@]}"; do
  if [ ! -f "$file" ]; then
    missing_files+=("$file")
  fi
done

if [ ${#missing_files[@]} -gt 0 ]; then
  echo "エラー: 以下のファイルが見つかりません:"
  for file in "${missing_files[@]}"; do
    echo "  - $file"
  done
  exit 1
fi

# ファイルを結合
cat "${files[@]}" > "$OUTPUT_FILE"

# 結果を表示
if [ -f "$OUTPUT_FILE" ]; then
  line_count=$(wc -l < "$OUTPUT_FILE")
  file_size=$(du -h "$OUTPUT_FILE" | cut -f1)
  
  echo "✓ 結合完了: $OUTPUT_FILE"
  echo "  行数: $line_count"
  echo "  ファイルサイズ: $file_size"
  echo ""
  echo "次のステップ:"
  echo "  chmod +x scripts/convert_chapters_to_word.sh"
  echo "  ./scripts/convert_chapters_to_word.sh"
else
  echo "✗ 結合に失敗しました"
  exit 1
fi

echo ""
echo "========================================="
echo "✓ 完了"
echo "========================================="
