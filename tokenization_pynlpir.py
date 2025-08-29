import pynlpir, json

pynlpir.open()
lis = []
with open('qiangqiang.txt', 'r', encoding='utf-8') as text:
    sens = text.readlines()
    for i in sens:
        lis.append(pynlpir.segment(i, pos_tagging=False))
tokens = sum(lis, [])
with open('types_pynlpir.json', 'w', encoding='utf-8') as t:
    a = list(set(tokens))
    a.pop()
    json.dump(list(set(tokens)), t, ensure_ascii=False, indent = 0)
pynlpir.close()