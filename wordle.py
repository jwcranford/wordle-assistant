#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description='''
wordle.py processes the given word list file, calculates the
frequency of each letter, then scores each word accordingly.
It prints the same word list along with the score of each word.''')

parser.add_argument("file", help='word list, one word per line. For example, /usr/share/dict/words')
parser.add_argument("-f", '--print_frequencies',
    help="print letter frequencies and exit",
    action='store_true')
parser.add_argument('-s', '--print_scores', 
    help='score the words in the file and print them, with highest scores first',
    action='store_true')
parser.add_argument('-t', '--top',
    help='number of top scoring words to print',
    default=10,
    type=int)

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
    for c in set(word):
        sum += freq.get(c, 0)
    return sum

def print_top(scores):
    print(f"{len(scores)} words left")
    for (w,s) in scores[0:args.top]:
        print(f"{w}: {s}")

with open(args.file) as f:
    words = [word.strip() for word in f]
    freq = frequencies(words)
    scores = [(word, score(freq, word)) for word in words]
    scores.sort(key=lambda s: s[1],
        reverse=True)
    
if (args.print_frequencies):
    for ci in range(ord('A'), ord('Z')):
        c = chr(ci)
        print(f"{c}: {freq[c]}")
elif (args.print_scores):
    for (w, s) in scores:
        print(f"{w}: {s}")
else:
    print_top(scores)


