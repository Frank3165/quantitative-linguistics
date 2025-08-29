import json
from pypinyin import lazy_pinyin, Style

with open('types_pynlpir.json', 'r', encoding='utf-8') as f:
    types = json.load(f)

def distribution(n):
    num = 0
    dic1, dic2, dic3 = {}, {}, {}
    for i in n:
        finals = lazy_pinyin(i, style=Style.FINALS)
        inits = lazy_pinyin(i, style=Style.INITIALS, strict=True)
        num = 0
        for s in finals:
            if s[-1] == 'g':
                num += len(s) - 1
            elif s[-2:] in ('ai', 'ei', 'ao', 'ou'):
                num += len(s) - 1
            else:
                num += len(s)
        for z in inits:
            if len(z) == 0:
                pass
            else:
                num += 1
        dic1[num] = dic1.get(num, 0) + 1
        dic2[len(i)] = dic2.get(len(i), 0) + 1
        dic3[len(i)] = dic3.get(len(i), 0) + num
    phones = sorted(dic1.items(), key=lambda x:int(x[0]))
    characters = sorted(dic2.items(), key=lambda x:int(x[0]))
    syllable_phone = sorted(dic3.items(), key=lambda x:int(x[0]))
    return phones, characters, syllable_phone

def altmann (items, file):
    for i in items:
        file.write(f'{i[0]}\t{i[1]}\n')

with open('syllable_phone_static_new.txt', 'w') as sps:
    c, d, z = distribution(types)
    h = [(k1, v1 / v2 / k1) for (k1, v1), (k2, v2) in zip(z, d)]
    altmann(h, sps)
