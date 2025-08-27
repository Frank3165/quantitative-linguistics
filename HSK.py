import char2pinyin
with open('HSK_words_2021.txt', 'r', encoding='utf-8') as hsk:
    chars = [i.rstrip('\n') for i in hsk.readlines()]
a, b, c = char2pinyin.distribution(chars)
with open('syllable_phone_HSK.txt', 'w', encoding='utf-8') as sph:
    z = [(k1, v1 / v2 / k1) for (k1, v1), (k2, v2) in zip(c, b)]
    char2pinyin.altmann(z, sph)