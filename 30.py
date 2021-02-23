'''
https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
30 - Pick Word 1/3

In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. 
Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. 
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.
Aside: what is SOWPODS?
SOWPODS is a word list commonly used in word puzzles and games (like Scrabble for example). It is the combination of the Scrabble Player’s Dictionary and the Chamber’s Dictionary.
'''
import random
def pick_word():
    with open("sowpods.txt") as fh:
        words = list(fh)
    return random.choice(words)