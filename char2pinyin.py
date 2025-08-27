import json
from pypinyin import lazy_pinyin, Style

with open('tokens.json', 'r', encoding='utf-8') as f:
    tokens = json.load(f)
types = set(tokens)

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

with open('phones_dynamic.txt', 'w') as pd, \
    open('characters_dynamic.txt', 'w') as cd, \
    open('phones_static.txt', 'w') as ps, \
    open('characters_static.txt', 'w') as cs, \
    open('phones_average.txt', 'w') as pa, \
    open('characters_average.txt', 'w') as ca, \
    open('syllable_phone_dynamic.txt', 'w') as spd, \
    open('syllable_phone_static.txt', 'w') as sps:
    a, b, y = distribution(tokens)
    c, d, z = distribution(types)
    e = [(k1, v1 / v2) for (k1, v1), (k2, v2) in zip(a, c)]
    f = [(k1, v1 / v2) for (k1, v1), (k2, v2) in zip(b, d)]
    g = [(k1, v1 / v2 / k1) for (k1, v1), (k2, v2) in zip(y, b)]
    h = [(k1, v1 / v2 / k1) for (k1, v1), (k2, v2) in zip(z, d)]
    altmann(a, pd)
    altmann(b, cd)
    altmann(c, ps)
    altmann(d, cs)
    altmann(e, pa)
    altmann(f, ca)
    altmann(g, spd)
    altmann(h, sps)
