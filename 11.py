'''
https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
Exercise 11 - Check Primality Functions
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions.
'''
num = int(input("Enter a number: "))
no_of_diviser = 0
for i in range(2, num):
    if num % i == 0:
        no_of_diviser += 1
if no_of_diviser <= 0:
    print("The number", num, "is prime.")
else:
    print("The number", num, "is not prime.")