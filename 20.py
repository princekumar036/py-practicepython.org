'''
https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
20 - Element Search
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:
Use binary search.
'''
def is_in_list(lst, no):
    if no in lst:
        return True
    else:
        return False