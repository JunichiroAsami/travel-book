#!/bin/bash
# backup_manual.sh - 手動バックアップスクリプト

# バックアップ対象ディレクトリ
PROJECT_DIR="/home/ubuntu/vietnam_thailand_writing_program"

# バックアップファイル名（日時付き）
BACKUP_FILE="/home/ubuntu/project_backup_$(date +%Y%m%d_%H%M%S).zip"

# zipで圧縮
cd /home/ubuntu
zip -r "$BACKUP_FILE" vietnam_thailand_writing_program/ \
    -x "*.git/*" \
    -x "*/archive/*" \
    -x "*/node_modules/*" \
    -x "*/project_full/*" \
    -q

echo "=========================================="
echo "バックアップ完了"
echo "=========================================="
echo "ファイル: $BACKUP_FILE"
echo "サイズ: $(du -h "$BACKUP_FILE" | cut -f1)"
echo ""
echo "次のステップ:"
echo "1. このファイルをダウンロードしてください"
echo "2. OneDriveまたはGoogle Driveにアップロードしてください"
echo "=========================================="
