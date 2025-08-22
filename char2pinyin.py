import json
from pypinyin import lazy_pinyin
with open('tokens_spacy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
chars = sum(data, [])
num = 0
dic = {}
for i in chars:
    lis = lazy_pinyin(i)
    num = 0
    for pinyin in lis:
        if pinyin[0] in 'bpmfdtnlgkhjqxrzcs':
            if pinyin[1] == 'h':
                if pinyin[-1] == 'g':
                    num += len(pinyin) - 2
                else:
                    num += len(pinyin) - 1
            elif pinyin[-1] == 'g':
                num += len(pinyin) - 1
            else:
                num += len(pinyin)
        elif pinyin[0] in 'wy':
            if pinyin[1] == 'a':
                if pinyin == 'yuan':
                    num += len(pinyin) - 1
                else:
                    num += len(pinyin)
            elif pinyin == 'wu' or 'yi' or 'yv':
                num += 1
            elif pinyin[-1] == 'g':
                if pinyin == 'yong':
                    num += 3
                else:
                    num += 2
            else:
                num += 2
        else:
            if pinyin[-1] == 'g':
                num += len(pinyin) - 1
            else:
                num += len(pinyin)
    dic[str(num)] = dic.get(str(num), 0) + 1
print(sorted(dic.items(), key=lambda x:int(x[0])))