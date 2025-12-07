#!/usr/bin/env python3
"""
LOG形式の引用ブロックをパターン1（コードブロック形式）に変換するスクリプト
"""

import re
import sys

def convert_log_quote_to_code_block(content):
    """
    LOG形式の引用ブロックをコードブロック形式に変換
    
    変換前:
    > **【LOG番号: タイトル】**
    > USER: 質問内容
    > ASSISTANT: 回答内容
    
    変更後:
    著者は、AIに対して以下のように質問した。
    
    ```
    【プロンプト】
    質問内容
    
    ChatGPT:
    回答内容
    ```
    
    （LOG番号: タイトル）
    """
    
    # パターン: LOG形式の引用ブロックを検出
    pattern = r'> \*\*【(LOG[^】]+)】\*\*\s*\n> USER: ([^\n]+)\s*\n> ASSISTANT: (.+?)(?=\n\n|\n> \*\*【|$)'
    
    def replace_func(match):
        log_info = match.group(1)
        user_text = match.group(2).strip()
        assistant_text = match.group(3).strip()
        
        # パターン1形式に変換
        result = f"""著者は、AIに対して以下のように質問した。

```
【プロンプト】
{user_text}

ChatGPT:
{assistant_text}
```

（{log_info}）"""
        
        return result
    
    # 変換実行
    converted = re.sub(pattern, replace_func, content, flags=re.MULTILINE | re.DOTALL)
    
    return converted

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 convert_prompt_format_log.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # ファイル読み込み
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 変換
    converted = convert_log_quote_to_code_block(content)
    
    # ファイル書き込み
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted)
    
    print(f"変換完了: {input_file} -> {output_file}")

if __name__ == '__main__':
    main()
