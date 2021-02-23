'''
https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html
31 - Guess Letters 2/3
Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. 
The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. 
For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. 
Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.
'''
import re
def guess_letters():
    count = 0
    generated_word = "EVAPORATE"
    guessed = list("_" * len(generated_word))
    print("Welcome to Hangman!")
    print(" ".join(guessed))
    while "_" in guessed:
        ltr = input("Guess your letter: ").upper()
        ltr_indexes = [m.start() for m in re.finditer(ltr, generated_word)]
        if ltr in guessed:
            print("Guessed already")
        elif len(ltr_indexes) > 0:
            for i in ltr_indexes:
                guessed[i] = ltr
            print(" ".join(guessed))
            count += 1
        else:
            print("Incorrect!")
            count += 1
    print(f"You guessed it right in {count} times.")
