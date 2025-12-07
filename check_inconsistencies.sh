#!/bin/bash

echo "=== 不整合チェック開始 ==="
echo ""

# 1. 統合原稿のバージョンと文字数
echo "【1】統合原稿のバージョンと文字数"
echo "---"
echo "progress_report_v8.md:"
grep -E "complete_manuscript|文字数" project_management/progress_report_v8.md | head -5
echo ""
echo "実際のファイル:"
ls -lh finals/complete_manuscript*.md 2>/dev/null
echo ""
for file in finals/complete_manuscript*.md; do
    if [ -f "$file" ]; then
        chars=$(wc -m < "$file")
        echo "$(basename $file): ${chars}文字"
    fi
done
echo ""

# 2. 付録Aの収録LOG数
echo "【2】付録Aの収録LOG数"
echo "---"
echo "progress_report_v8.md:"
grep -A 1 "付録A" project_management/progress_report_v8.md | grep -E "LOG|件"
echo ""
echo "log_coverage_improvement_report.md:"
grep -E "付録A.*LOG|収録LOG数" log_coverage_improvement_report.md | head -3
echo ""
echo "実際のファイル:"
if [ -f "log_coverage_improvement/appendix_a_expanded.md" ]; then
    count=$(grep -c "^### LOG" log_coverage_improvement/appendix_a_expanded.md)
    echo "appendix_a_expanded.md: ${count}件"
fi
if [ -f "drafts/appendix_a_final.md" ]; then
    count=$(grep -c "^### LOG" drafts/appendix_a_final.md)
    echo "appendix_a_final.md: ${count}件"
fi
echo ""

# 3. 改善提案の状況
echo "【3】改善提案の状況"
echo "---"
echo "progress_report_v8.md: 改善提案の承認待ち"
echo ""
echo "v13_implementation_report.md:"
grep -E "改善提案.*完了|✅" v13_implementation_report.md | head -5
echo ""
echo "log_coverage_improvement_report.md:"
grep -E "改善提案.*完了|✅" log_coverage_improvement_report.md | head -5
echo ""

# 4. 統合原稿の最新バージョン
echo "【4】統合原稿の最新バージョン"
echo "---"
echo "progress_report_v8.md: complete_manuscript.md (168,656文字)"
echo "v13_implementation_report.md: complete_manuscript_v13.md (192,837文字)"
echo ""
echo "実際のファイル:"
ls -lh finals/complete_manuscript*.md 2>/dev/null | awk '{print $9, $5}'
echo ""

# 5. プログレスレポートのバージョン
echo "【5】プログレスレポートのバージョン"
echo "---"
ls -lt project_management/progress_report*.md | head -3 | awk '{print $9, $6, $7, $8}'
echo ""

echo "=== 不整合チェック完了 ==="
