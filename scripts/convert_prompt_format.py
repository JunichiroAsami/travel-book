#!/usr/bin/env python3
"""
引用ブロック形式をパターン1（コードブロック形式）に変換するスクリプト
"""

import re
import sys

def convert_quote_to_code_block(content):
    """
    引用ブロック形式をコードブロック形式に変換
    
    変換前:
    > **著者の質問**:
    > 「質問内容」
    
    > **AIの回答**:
    > 「回答内容」
    
    変換後:
    著者は、AIに対して以下のように質問した。
    
    ```
    【プロンプト】
    質問内容
    
    ChatGPT:
    回答内容
    ```
    """
    
    # パターン: 引用ブロック形式の質問と回答を検出
    pattern = r'> \*\*著者の質問\*\*:\s*\n((?:> .*\n)+)\s*\n> \*\*AIの回答\*\*:\s*\n((?:> .*\n?)+)'
    
    def replace_func(match):
        question_lines = match.group(1)
        answer_lines = match.group(2)
        
        # 引用記号（> ）を削除
        question = '\n'.join(line[2:] if line.startswith('> ') else line 
                            for line in question_lines.strip().split('\n'))
        answer = '\n'.join(line[2:] if line.startswith('> ') else line 
                          for line in answer_lines.strip().split('\n'))
        
        # 「」を削除（質問の場合のみ）
        question = question.strip()
        if question.startswith('「') and question.endswith('」'):
            question = question[1:-1]
        
        # 回答の「」も削除
        answer = answer.strip()
        if answer.startswith('「') and answer.endswith('」'):
            answer = answer[1:-1]
        
        # パターン1形式に変換
        result = f"""著者は、AIに対して以下のように質問した。

```
【プロンプト】
{question}

ChatGPT:
{answer}
```"""
        
        return result
    
    # 変換実行
    converted = re.sub(pattern, replace_func, content, flags=re.MULTILINE)
    
    return converted

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 convert_prompt_format.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # ファイル読み込み
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 変換
    converted = convert_quote_to_code_block(content)
    
    # ファイル書き込み
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted)
    
    print(f"変換完了: {input_file} -> {output_file}")

if __name__ == '__main__':
    main()
