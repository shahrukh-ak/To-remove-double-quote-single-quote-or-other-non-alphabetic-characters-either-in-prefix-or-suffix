#!/usr/bin/python
from string import ascii_letters
import sys

for lines in sys.stdin:
    lines = lines.strip().split(' ')
    for words in lines:
        words = ''.join(filter(lambda x: x in ascii_letters, words)).lower()
        print("%s\t%s"%(words, 1))

