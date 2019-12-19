#!/usr/bin/python
from sys import stdin

def word_count(n): return n[1]


words = []

(last_key, count) = (None, 0)
for line in stdin:
    (key, value) = line.split('\t')
    if last_key and key != last_key:
        words.append((last_key, count))
        (last_key, count) = (key, int(value))
    else:
        (last_key, count) = (key, count + 1)
if last_key:
    words.append((last_key, count))

words.sort(key=word_count, reverse=True)

for x in range(10):
    print('%s\t%s' % (words[x][0], words[x][1]))
