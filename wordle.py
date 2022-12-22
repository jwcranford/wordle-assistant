#!/usr/bin/env python3

import sys

def usage():
    print(f"{sys.argv[0]} processes the given word list file, calculates the ")
    print('frequency of each letter, then scores each word accordingly.')
    print('It prints the same word list along with the score of each word.')
    print()
    print(f"Usage: {sys.argv[0]} word-list")

if (len(sys.argv) < 2):
    usage()
    sys.exit(1)

def frequencies(words):
    freq = {}
    for word in words:
        for ltr in set(word):
            if freq.get(ltr) == None:
                freq[ltr] = 1
            else:
                freq[ltr] = freq[ltr] + 1
    return freq

with open(sys.argv[1]) as f:
    words = [word.strip() for word in f]
    freq = frequencies(words)
    
# print frequency table
for ci in range(ord('A'), ord('Z')):
    c = chr(ci)
    print(f"{c}: {freq[c]}")
