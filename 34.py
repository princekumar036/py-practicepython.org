'''
https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
34 - Birthday Json 2/4
In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.
'''
import json

def add_bday():
    new = dict()
    name = input("Enter scientist's name: ")
    dob = input("Enter scientist's dob: (DD/MM/YYYY) ")
    new[name] = dob
    with open("scientistbdays.json", mode="a") as f:
        json.dump(new, f)
    print("Birthday added sucessfully!")

def find_bday():
    name = input("Enter the name of a scientist: ")
    with open("scientistbdays.json", "r") as f:
        file = json.load(f)
        search_result = file.get(name, "Not Found")
        if search_result != "Not Found":
            print(f"{name}'s date of birthday is", search_result)
        else:
            add = input(f"Do you want to add {name}'s birthday to the dictionary? (Y/N) ").upper()
            if add == "Y":
                add_bday()
            else:
                print("Thank You!")

find_bday()