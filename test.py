from pypinyin import lazy_pinyin, Style

i = '百分之十几二十几'
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
print(num)