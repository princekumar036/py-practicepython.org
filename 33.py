'''
https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
33 - Birthday Dictionaries 1/4
For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
'''
bday_dict = {
    "Albert Einstein": "09/01/1991",
    "Benjamin Franklin" : "09/01/1992",
    "Ada Lovelace": "09/01/1993"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for k in bday_dict:
    print(k)

name = input("Who's birthday do you want to look up? ")
print(f"{name}'s birthday is {bday_dict[name]}")