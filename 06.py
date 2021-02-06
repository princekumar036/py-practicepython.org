'''
Exercise 6 - String Lists  
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''
str = input("Enter a string: ")
if str == str[::-1]:
    print(f"Ther string {str} is a palindrome.")
else:
    print(f"Ther string {str} is NOT a palindrome.")