'''
Exercise 1 - Character Input
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
-Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
-Print out that many copies of the previous message on separate lines.
'''
name = input("Enter your name: ")
age = input("Enter your age: ")
# print(f"Hello {name}, you will be 100 years old in {2020-int(age)+100}.")
num = int(input("Enter a number: "))
print(f"Hello {name}, you will be 100 years old in {2020-int(age)+100}.\n" * num)