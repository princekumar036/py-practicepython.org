'''
https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
Write a program (function!) that takes a list and returns a new list that 
contains all the elements of the first list minus all the duplicates.

Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
def non_duplicate_list(input_list):
    new_list = []
    for elem in input_list:
        if elem not in new_list:
            new_list.append(elem)
    return new_list

    # using sets
# def non_duplicate_list(input_list):
#     return list(set(input_list))