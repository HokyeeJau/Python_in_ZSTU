# !pip install jieba
import jieba
import jieba.analyse
import re
from collections import Counter

file = '/三国演义.txt'
txt = open(file, 'r', encoding='utf-8').read()
txt = re.sub(r'\s+', r' ', txt)
txt = re.sub(r'\.+', r' ', txt)
tags = jieba.analyse.extract_tags(txt, topK=100)
words = jieba.cut(txt)
counter = Counter()
for word in words: 
    if word in tags:
        counter[word] += 1
result = counter.most_common()

for i in range(1, 21):
    key, value = result[i]
    print('{:<3}{:<6}{:>5}'.format(i, key, value))
