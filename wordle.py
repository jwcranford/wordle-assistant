#!/usr/bin/env python3

import sys
import argparse

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

def print_top(scores, top):
    print(f"{len(scores)} words left")
    for (w,s) in scores[0:top]:
        print(f"{w}: {s}")

def next_guess():
    while True:
        print('Enter next guess and results. Example: RAISE GyyG. means that R and S are green, A and I are yellow, and E is black')
        g = input('Guess:  ')
        r = input('Result: ')
        if len(g) != len(r):
            continue
        else:
            return zip(g, r)

def process_guess(words, guess):
    i = 0
    for (g,r) in guess:
        match r:
            # If black, Remove all words containing g
            case '.':
                words = [w for w in words if not g in w]
            # If yellow
            #    * Remove all words without g
            #    * Remove all words with g in current position
            case 'y':
                words = [w for w in words if g in w and w[i] != g]
            # If green, Remove all words without g in current position
            case 'G':
                  words = [w for w in words if w[i] == g]
        i = i + 1
    return words

if __name__ == '__main__':
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
        while True:
            print_top(scores, args.top)
            guess = next_guess()
            words = process_guess(words, guess)
            freq = frequencies(words)
            scores = [(word, score(freq, word)) for word in words]
            scores.sort(key=lambda s: s[1],
                reverse=True)
