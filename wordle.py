#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description='''
wordle.py processes the given word list file, calculates the
frequency of each letter, then scores each word accordingly.
It prints the same word list along with the score of each word.''')

parser.add_argument("file", help='word list, one word per line. For example, /usr/share/dict/words')
parser.add_argument("-f", '--frequencies', help="print letter frequencies and exit",
    action='store_true')

args = parser.parse_args()

def frequencies(words):
    freq = {}
    for word in words:
        for ltr in set(word):
            if freq.get(ltr) == None:
                freq[ltr] = 1
            else:
                freq[ltr] = freq[ltr] + 1
    return freq

def score(freq, word):
    sum = 0
    for c in word:
        sum += freq.get(c, 0)
    return sum

with open(args.file) as f:
    words = [word.strip() for word in f]
    freq = frequencies(words)
    

if (args.frequencies):
    for ci in range(ord('A'), ord('Z')):
        c = chr(ci)
        print(f"{c}: {freq[c]}")