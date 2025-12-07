#!/bin/bash

echo "=== 残存する不整合のあるドキュメント ==="
echo ""

echo "1. 各章の完了レポート:"
find finals -name "*_completion_report.md" 2>/dev/null | sort
echo ""

echo "2. レビュー関連ドキュメント:"
ls -1 reviews/*.md 2>/dev/null | sort
echo ""

echo "3. WBS:"
ls -1 planning/wbs*.md 2>/dev/null | sort
echo ""

echo "4. 進捗・課題管理レポート:"
ls -1 project_management/*.md 2>/dev/null | sort
echo ""

