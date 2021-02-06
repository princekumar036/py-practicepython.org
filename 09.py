'''
Exercise 9 - Guessing Game 1
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random
while True:
    no_random = random.randint(1, 9)
    guess = input("What's your guess: ")
    if guess == "exit":
        break
    else:
        no_guess = int(guess)
        if no_guess == no_random:
            print("Exactly right. Random No", no_random)
        elif no_guess > no_random:
            print("Too hight. Random No", no_random)
        else:
            print("Too low. Random No", no_random)