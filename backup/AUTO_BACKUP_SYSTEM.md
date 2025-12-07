# 自動バックアップシステム設計書

**作成日**: 2025-11-24  
**バージョン**: 1.0

---

## 1. 目的

サンドボックスリセットによるデータ損失を防ぐため、プロジェクトの重要なファイルとスレッドの経緯を定期的に外部ストレージ（OneDrive、Google Drive）にバックアップする自動システムを構築する。

---

## 2. バックアップ対象

### 2.1 重要度：最高（必須バックアップ）

以下のファイルは、プロジェクトの根幹であり、損失すると復旧が困難なため、最優先でバックアップする：

| カテゴリ | ファイル | パス |
|:---|:---|:---|
| 書籍企画書 | `book_proposal.md` | `/home/ubuntu/vietnam_thailand_writing_program/planning/` |
| WBS | `wbs_v3.md` | `/home/ubuntu/vietnam_thailand_writing_program/planning/` |
| 詳細設計書（全12章） | `chapter{1-12}_detailed_design_v2.md` | `/home/ubuntu/vietnam_thailand_writing_program/planning/` |
| 素材ファイル（全9章） | `chapter{1-9}_materials_v2.md` | `/home/ubuntu/vietnam_thailand_writing_program/planning/materials/` |
| 会話ログ索引 | `conversation_index_v2.md` | `/home/ubuntu/vietnam_thailand_writing_program/materials/` |
| 巨大素材DB | `giant_material_database.md` | `/home/ubuntu/vietnam_thailand_writing_program/materials/` |
| 全29記事レポート | `all_29_articles_report.md` | `/home/ubuntu/vietnam_thailand_writing_program/materials/` |

### 2.2 重要度：高（推奨バックアップ）

以下のファイルは、作業の進捗や品質に関わるため、定期的にバックアップする：

| カテゴリ | ファイル | パス |
|:---|:---|:---|
| 初稿（全章） | `chapter{1-12}_draft.md` | `/home/ubuntu/vietnam_thailand_writing_program/drafts/` |
| 最終稿（全章） | `chapter{1-12}_final.md` | `/home/ubuntu/vietnam_thailand_writing_program/finals/` |
| 進捗管理表 | `progress_report_v2.md` | `/home/ubuntu/vietnam_thailand_writing_program/project_management/` |
| 課題管理表 | `issue_tracker.md` | `/home/ubuntu/vietnam_thailand_writing_program/project_management/` |

### 2.3 重要度：中（定期バックアップ）

以下のファイルは、参照用であり、損失しても再作成可能なため、定期的にバックアップする：

| カテゴリ | ファイル | パス |
|:---|:---|:---|
| 業務標準化ドキュメント | `writing_standardization/` 全体 | `/home/ubuntu/vietnam_thailand_writing_program/writing_standardization/` |
| バックアップ対策ドキュメント | `backup/` 全体 | `/home/ubuntu/vietnam_thailand_writing_program/backup/` |

### 2.4 スレッド履歴

以下のドキュメントは、スレッドのやり取りを記録したものであり、定期的に更新してバックアップする：

| カテゴリ | ファイル | パス |
|:---|:---|:---|
| スレッド履歴 | `THREAD_HISTORY_DETAILED.md` | `/home/ubuntu/vietnam_thailand_writing_program/backup/` |
| プロジェクト整理報告 | `PROJECT_ORGANIZATION_REPORT.md` | `/home/ubuntu/vietnam_thailand_writing_program/backup/` |
| リセット原因分析 | `SANDBOX_RESET_ANALYSIS.md` | `/home/ubuntu/vietnam_thailand_writing_program/backup/` |

---

## 3. バックアップ先

### 3.1 OneDrive

**利点**:
- Microsoftアカウントで簡単にアクセス可能
- 大容量（5GB～1TB）
- バージョン履歴管理が可能

**欠点**:
- APIアクセスには認証が必要
- 無料プランは5GBまで

**推奨用途**: 個人用バックアップ、小規模プロジェクト

### 3.2 Google Drive

**利点**:
- Googleアカウントで簡単にアクセス可能
- 大容量（15GB～2TB）
- バージョン履歴管理が可能
- Google Workspace統合

**欠点**:
- APIアクセスには認証が必要
- 無料プランは15GBまで

**推奨用途**: チーム共有、大規模プロジェクト

### 3.3 両方を使用（推奨）

**戦略**:
- **OneDrive**: 最重要ファイル（詳細設計書、素材ファイル）
- **Google Drive**: 全ファイル（プロジェクト全体）

**利点**:
- 冗長性が高く、一方が失敗しても他方で復旧可能
- 両方のエコシステムを活用できる

---

## 4. バックアップ頻度

### 4.1 リアルタイムバックアップ

以下のタイミングで即座にバックアップを実行する：

- **重要ファイルの作成・更新時**: 詳細設計書、素材ファイル、初稿、最終稿
- **スレッド履歴の更新時**: `THREAD_HISTORY_DETAILED.md` の更新

### 4.2 定期バックアップ

以下のスケジュールで定期的にバックアップを実行する：

- **毎日1回**: 全ファイルのバックアップ（深夜0時）
- **毎週1回**: プロジェクト全体のフルバックアップ（日曜日深夜）

### 4.3 手動バックアップ

以下のタイミングで手動バックアップを実行する：

- **重要なマイルストーン達成時**: 章の完成、フェーズの完了
- **サンドボックスリセット前**: 長時間の中断前

---

## 5. バックアップ方法

### 5.1 方法1: Manus標準機能を使用（推奨）

Manusには、ファイルをアップロードする機能があるため、これを活用する。

**手順**:
1. バックアップ対象ファイルをzipで圧縮
2. ユーザーにzipファイルをダウンロードしてもらう
3. ユーザーがOneDriveまたはGoogle Driveにアップロード

**利点**:
- シンプルで確実
- 外部APIに依存しない

**欠点**:
- 手動操作が必要
- 自動化が困難

### 5.2 方法2: rcloneを使用（自動化）

`rclone`は、OneDriveやGoogle Driveと同期できるコマンドラインツールです。

**手順**:
1. サンドボックスに`rclone`をインストール
2. OneDriveまたはGoogle Driveの認証を設定
3. バックアップスクリプトを作成し、定期実行

**利点**:
- 完全自動化が可能
- 双方向同期が可能

**欠点**:
- 認証設定が複雑
- サンドボックスリセット時に再設定が必要

### 5.3 方法3: GitHub/GitLabを使用（バージョン管理）

GitHubまたはGitLabにプロジェクトをプッシュし、バージョン管理とバックアップを兼ねる。

**手順**:
1. GitHubまたはGitLabにリポジトリを作成
2. プロジェクトをgit initし、リモートリポジトリに接続
3. 定期的にgit commit & pushを実行

**利点**:
- バージョン履歴が完全に保持される
- 複数人での共同作業が可能
- 無料プランで十分な容量

**欠点**:
- git操作の知識が必要
- 大きなバイナリファイルには不向き

---

## 6. 推奨バックアップ戦略

### 6.1 短期的な対策（即座に実施）

**方法1: 手動バックアップ**を使用

1. プロジェクト全体をzipで圧縮
2. ユーザーにダウンロードしてもらう
3. ユーザーがOneDriveまたはGoogle Driveにアップロード

**実施頻度**: 
- 重要なファイルを作成・更新した直後
- 作業セッション終了時

### 6.2 中長期的な対策（今後実装）

**方法3: GitHubを使用**（推奨）

1. GitHubにプライベートリポジトリを作成
2. プロジェクトをgit管理下に置く
3. 定期的にcommit & pushを実行

**実施頻度**:
- 毎日1回（自動）
- 重要なマイルストーン達成時（手動）

**補完**: 
- **方法2: rclone**を併用し、OneDriveまたはGoogle Driveにも同期

---

## 7. バックアップスクリプトの実装

### 7.1 手動バックアップスクリプト

```bash
#!/bin/bash
# backup_manual.sh - 手動バックアップスクリプト

# バックアップ対象ディレクトリ
PROJECT_DIR="/home/ubuntu/vietnam_thailand_writing_program"

# バックアップファイル名（日時付き）
BACKUP_FILE="project_backup_$(date +%Y%m%d_%H%M%S).zip"

# zipで圧縮
cd /home/ubuntu
zip -r "$BACKUP_FILE" vietnam_thailand_writing_program/ \
    -x "*.git/*" \
    -x "*/archive/*" \
    -x "*/node_modules/*"

echo "バックアップ完了: $BACKUP_FILE"
echo "ファイルをダウンロードして、OneDriveまたはGoogle Driveにアップロードしてください。"
```

**使用方法**:
```bash
bash /home/ubuntu/vietnam_thailand_writing_program/backup/backup_manual.sh
```

### 7.2 自動バックアップスクリプト（GitHub使用）

```bash
#!/bin/bash
# backup_auto_github.sh - 自動バックアップスクリプト（GitHub）

# プロジェクトディレクトリ
PROJECT_DIR="/home/ubuntu/vietnam_thailand_writing_program"

# GitHubリポジトリURL（要設定）
GITHUB_REPO="https://github.com/username/project.git"

# プロジェクトディレクトリに移動
cd "$PROJECT_DIR"

# gitリポジトリの初期化（初回のみ）
if [ ! -d ".git" ]; then
    git init
    git remote add origin "$GITHUB_REPO"
fi

# 変更をステージング
git add .

# コミット
git commit -m "Auto backup: $(date +%Y-%m-%d\ %H:%M:%S)"

# プッシュ
git push origin main

echo "GitHubへの自動バックアップ完了"
```

**使用方法**:
```bash
bash /home/ubuntu/vietnam_thailand_writing_program/backup/backup_auto_github.sh
```

### 7.3 スレッド履歴更新スクリプト

```bash
#!/bin/bash
# update_thread_history.sh - スレッド履歴更新スクリプト

# スレッド履歴ファイル
THREAD_HISTORY="/home/ubuntu/vietnam_thailand_writing_program/backup/THREAD_HISTORY_DETAILED.md"

# 現在の日時
CURRENT_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# スレッド履歴に新しいエントリを追加
echo "" >> "$THREAD_HISTORY"
echo "---" >> "$THREAD_HISTORY"
echo "" >> "$THREAD_HISTORY"
echo "### 更新: $CURRENT_TIME" >> "$THREAD_HISTORY"
echo "" >> "$THREAD_HISTORY"
echo "**実施内容**:" >> "$THREAD_HISTORY"
echo "- （ここに実施内容を記載）" >> "$THREAD_HISTORY"
echo "" >> "$THREAD_HISTORY"

echo "スレッド履歴を更新しました"
```

---

## 8. 復元手順

### 8.1 OneDrive/Google Driveからの復元

**手順**:
1. OneDriveまたはGoogle Driveから最新のバックアップzipファイルをダウンロード
2. Manusにzipファイルをアップロード
3. サンドボックス内でzipファイルを解凍
4. プロジェクトディレクトリを確認

**コマンド例**:
```bash
cd /home/ubuntu
unzip project_backup_20251124_120000.zip
cd vietnam_thailand_writing_program
ls -la
```

### 8.2 GitHubからの復元

**手順**:
1. サンドボックス内でgit cloneを実行
2. プロジェクトディレクトリを確認

**コマンド例**:
```bash
cd /home/ubuntu
git clone https://github.com/username/project.git vietnam_thailand_writing_program
cd vietnam_thailand_writing_program
ls -la
```

---

## 9. 実装計画

### 9.1 フェーズ1: 手動バックアップ（即座に実施）

- [x] プロジェクト全体をzipで圧縮
- [ ] ユーザーにダウンロードしてもらう
- [ ] ユーザーがOneDriveまたはGoogle Driveにアップロード

### 9.2 フェーズ2: 自動バックアップスクリプトの作成（今後実装）

- [ ] `backup_manual.sh` を作成
- [ ] `backup_auto_github.sh` を作成
- [ ] `update_thread_history.sh` を作成

### 9.3 フェーズ3: GitHubリポジトリの設定（今後実装）

- [ ] GitHubにプライベートリポジトリを作成
- [ ] プロジェクトをgit管理下に置く
- [ ] 初回commit & pushを実行

### 9.4 フェーズ4: 定期実行の設定（今後実装）

- [ ] cronジョブを設定し、毎日自動バックアップを実行
- [ ] バックアップ成功/失敗の通知を設定

---

## 10. 結論

サンドボックスリセットによるデータ損失を防ぐため、以下の3層のバックアップ戦略を推奨します：

1. **即座の対策**: 手動バックアップ（zip + OneDrive/Google Drive）
2. **短期的な対策**: 自動バックアップスクリプト（GitHub）
3. **中長期的な対策**: 定期実行 + 冗長化（GitHub + OneDrive/Google Drive）

これにより、サンドボックスリセットが発生しても、最小限の損失で迅速に復旧できます。

---

**作成者**: Manus AI Agent  
**作成日時**: 2025年11月24日  
**バージョン**: 1.0
