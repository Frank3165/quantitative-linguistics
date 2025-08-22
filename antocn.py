import cn2an
with open('qiangqiang_raw.txt', 'r', encoding='utf-8') as t:
    sens = t.readlines()
with open('qiangqiang_an2cn.txt', 'w', encoding='utf-8') as s:
    for i in sens:
        s.write(cn2an.transform(i, 'an2cn'))
