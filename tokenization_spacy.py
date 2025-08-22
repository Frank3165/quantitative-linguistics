import spacy
import json
from pathlib import Path

def is_chinese_punct(char):
    # 中文标点unicode范围
    return (
        '\u3000' <= char <= '\u303F' or  # CJK 符号和标点
        '\uFF00' <= char <= '\uFFEF' or  # 全角符号
        char in "，。！？；：“”‘’（）《》【】、—…·"
    )

def filter_token(token):
    # 去除所有标点（含中文标点）和空白
    if token.is_punct or token.is_space:
        return False
    if any(is_chinese_punct(c) for c in token.text):
        return False
    return True

def cut_and_save_json(input_file, output_file):
    nlp = spacy.load("zh_core_web_sm")
    result = []
    with open(input_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            doc = nlp(line)
            tokens = [token.text for token in doc if filter_token(token)]
            if tokens:
                result.append(tokens)
    with open(output_file, 'w', encoding='utf-8') as fout:
        json.dump(result, fout, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    base = Path(__file__).parent
    input_path = base / "qiangqiang_final.txt"
    output_path = base / "tokens_spacy.json"
    cut_and_save_json(str(input_path), str(output_path))
    print(f"分词结果已保存为JSON文件：{output_path}")