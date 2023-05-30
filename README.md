# wordle-assistant

wordle-assistant is a Python command-line script that helps you play
Wordle. At each step in the game, wordle-assistant recomputes the next
best guess, based on an internal dictionary of words and the relative
frequencies of letters not yet guessed in the wordle game.

## Files

* README.md - this file
* wordle.py - where all the magic happens
* 5-letter-words - created from /usr/share/dict/words
* aspell-5-letter-words - created from the the en-common.wl file in the English 
dictionary available at https://ftp.gnu.org/gnu/aspell/dict/0index.html

### Creating a word list
```
$ cat {word-list} | egrep "^[a-zA-Z]{5}$" | tr a-z A-Z | sort -u 
```

In practice, I find that aspell-5-letter-words is more useful, as it 
contains less esoteric words, but your mileage may vary.

## Dependencies

wordle-assistant relies on a feature of Python 3.10, so Python 3.10+ must 
be installed.

## Usage
Typical usage:
```
$ ./wordle.py aspell-5-letter-words
```

Run `wordle.py -h` to see more details.
