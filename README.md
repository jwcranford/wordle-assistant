# wordle-companion

Companion program to wordle. wordle-companion is designed to be run in conjunction 
with a wordle game. At each step in the game, wordle-companion recomputes the next best guess,
based on an internal dictionary of words and the relative frequencies of letters
not yet guessed in the wordle game.

## Files

* README.md - this file
* wordle.py - where all the magic happens
* 5-letter-words.unique - created by these commands
```
$ egrep "^[a-zA-Z]{5}$" /usr/share/dict/words | tr a-z A-Z \
    | sort -u > 5-letter-words.unique
```

## Dependencies
wordle-companion relies on a feature of Python 3.10, so Python 3.10+ must be installed.

## Usage
Typical usage:
```
$ ./wordle.py -t 30 5-letter-words.unique
```

Run `wordle.py -h` to see more details.