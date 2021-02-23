'''
https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
32 - Hangman 3/3
In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
Optional additions:

# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!
'''
import random
def pick_word():
    with open("sowpods.txt") as fh:
        words = list(fh)
    return random.choice(words)


import re
def guess_letters():
    # variables initialisation
    attempts = 6
    generated_word = pick_word()
    guessed = list("_" * (len(generated_word)-1))
    guessed_letters = []

    print("Welcome to Hangman!")
    print(" ".join(guessed))

    while "_" in guessed and attempts > 0:

        ltr = input("Guess your letter: ").upper()

        if ltr in guessed_letters:
            print("Guessed already")
        else:
            guessed_letters.append(ltr)
            ltr_indexes = [m.start() for m in re.finditer(ltr, generated_word)]

            if len(ltr_indexes) > 0:
                for i in ltr_indexes:
                    guessed[i] = ltr
                print(" ".join(guessed))
                print("Corrrect! Attempts left:", attempts, end="\n\n")
            else:
                attempts -= 1
                print(" ".join(guessed))
                print("Incorrrect! Attempts left:", attempts, end="\n\n")

    if attempts == 0:
        print("Sorry! You ran out of attempts")
    else:
        print("Yay! You guessed it right!")
    
    another_game = input("Do you want to play another game (Y/N)? ").upper()
    if another_game == "Y":
        guess_letters()
    elif another_game == "N":
        print("Thank you for playing Hangman!")

guess_letters()
