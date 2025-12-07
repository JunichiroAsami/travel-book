# ChatGPTレビュー実施手順書

本書「AIツアーコンダクターと歩く ベトナム・タイ周遊記」の統合原稿v6を、ChatGPTでレビューする手順を説明します。

---

## 1. 必要なファイル

以下の2つのファイルをダウンロードしてください：

1. **統合原稿v6**: `complete_manuscript_v6.md`（10,889行）
   - 第1章～第12章
   - はじめに、おわりに
   - 付録の使い方ガイド
   - 付録A（WEB限定）- AIとの対話ログ集
   - 付録B - プロンプトテンプレート集
   - 付録C - AIツール総合ガイド

2. **レビュー依頼プロンプト**: `chatgpt_review_prompt_v6.txt`

---

## 2. ChatGPTでのレビュー手順

### 方法1：ChatGPT Web版（推奨）

1. **ChatGPT（https://chat.openai.com/）にアクセス**
   - ChatGPT Plus（有料版）を推奨（GPT-4を使用できるため）
   - 無料版でも可能ですが、回答の質が低下する可能性があります

2. **新しいチャットを開始**

3. **統合原稿v6をアップロード**
   - チャット画面の「📎」ボタンをクリック
   - `complete_manuscript_v6.md`をアップロード

4. **レビュー依頼プロンプトを貼り付け**
   - `chatgpt_review_prompt_v6.txt`の内容をコピー
   - チャット画面に貼り付けて送信

5. **レビュー結果を確認**
   - ChatGPTがレビュー結果を返します
   - 必要に応じて追加質問をします

6. **レビュー結果を保存**
   - レビュー結果をテキストファイルにコピー＆ペースト
   - ファイル名：`chatgpt_review_result_v6.txt`

---

### 方法2：ChatGPT API（上級者向け）

Pythonスクリプトを使って、ChatGPT APIでレビューを実施することもできます。

```python
import openai

# APIキーを設定
openai.api_key = "YOUR_API_KEY"

# 統合原稿を読み込み
with open("complete_manuscript_v6.md", "r", encoding="utf-8") as f:
    manuscript = f.read()

# レビュー依頼プロンプトを読み込み
with open("chatgpt_review_prompt_v6.txt", "r", encoding="utf-8") as f:
    review_prompt = f.read()

# ChatGPTにレビューを依頼
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "あなたは出版編集者です。"},
        {"role": "user", "content": f"{review_prompt}\n\n---\n\n{manuscript}"}
    ],
    temperature=0.3,
    max_tokens=4000
)

# レビュー結果を保存
with open("chatgpt_review_result_v6.txt", "w", encoding="utf-8") as f:
    f.write(response.choices[0].message.content)

print("レビュー完了！")
```

**注意**：
- APIキーは、OpenAIのWebサイトで取得してください
- GPT-4は有料です（入力トークン: $0.03/1K、出力トークン: $0.06/1K）
- 統合原稿v6は約10,889行（約300KB）なので、APIコストは約$3〜$5程度です

---

## 3. レビュー結果の確認と修正

1. **レビュー結果を確認**
   - `chatgpt_review_result_v6.txt`を開く
   - 「重大な問題」「軽微な問題」「改善提案」を確認

2. **修正が必要な箇所をリストアップ**
   - 問題箇所を章・節・項の番号でリストアップ
   - 修正案を確認

3. **各章ファイルを修正**
   - 統合原稿を直接修正せず、各章ファイル（`chapter1_final.md` ~ `chapter12_final.md`）を修正
   - 付録ファイルも同様に修正

4. **統合原稿を再作成**
   - 修正後の各章ファイルから、統合原稿v7を再作成

5. **再レビュー（必要に応じて）**
   - 修正後の統合原稿v7を、再度ChatGPTでレビュー

---

## 4. よくある質問

### Q1. ChatGPT無料版でもレビューできますか？

**A**: はい、可能です。ただし、GPT-3.5は回答の質が低下する可能性があります。重要なレビューには、ChatGPT Plus（GPT-4）を推奨します。

### Q2. 統合原稿が長すぎて、ChatGPTにアップロードできません

**A**: 統合原稿を分割してアップロードしてください。例えば、第1章〜第6章と第7章〜第12章に分割し、それぞれレビューを依頼します。

### Q3. ChatGPTのレビュー結果が抽象的すぎます

**A**: 追加質問で具体化してください。例：「第3章の問題箇所を、具体的な行番号とともに教えてください」

### Q4. レビュー結果が途中で切れてしまいました

**A**: 「続きを教えてください」と入力してください。ChatGPTは続きを返します。

---

## 5. レビュー後の次のステップ

1. **レビュー結果を筆者（Manus）に共有**
   - `chatgpt_review_result_v6.txt`をアップロード
   - 修正が必要な箇所を報告

2. **修正作業を実施**
   - 筆者（Manus）が各章ファイルを修正

3. **統合原稿v7を作成**
   - 修正後の各章ファイルから、統合原稿v7を再作成

4. **最終確認**
   - 統合原稿v7を最終確認
   - 必要に応じて再レビュー

---

## 6. まとめ

ChatGPTレビューは、出版前の最終チェックとして非常に有効です。厳しくレビューしてもらうことで、出版可能なレベルに達しているかを確認できます。

レビュー結果を受け取ったら、必ず修正作業を実施し、統合原稿v7を作成してください。

よろしくお願いいたします。
