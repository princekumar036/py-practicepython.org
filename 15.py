'''
https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
15 - Reverse Word Order
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. 
For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
'''
def reversed():
    str = input("Enter a sentance: ")
    return " ".join(str.split()[::-1])