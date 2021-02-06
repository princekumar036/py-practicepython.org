'''
https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
18 - Cows And Bulls
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. 
Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
'''
import random
def cow_bulls():
    generated_no = str(random.randint(1000, 10000))
    count = 0
    while True:
        cows = bulls = 0
        guessed_no = input("Guess the 4-digit number: ")
        for i in range(4):
            if guessed_no[i] in generated_no:
                bulls += 1
            if guessed_no[i] == generated_no[i]:
                cows += 1
                bulls -= 1
        print(cows, "cows,", bulls, "bulls")
        count += 1
        if guessed_no == generated_no:
            print("Bravo! You guessed in", count, "times.")
            break
        if guessed_no == "show":
            print("Alas! The right answer was", generated_no)
            break