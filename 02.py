'''
Exercise 2 - Odd Or Even
Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user. 

Extras:
-If the number is a multiple of 4, print out a different message.
-Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
num = int(input("Enter a number: "))
if num % 4 == 0:
    print(f"{num} is even and a multiple of 4")
elif num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")