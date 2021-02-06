'''
https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
23 - File Overlap
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. 
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia).
'''
def filetolist(fn):
    return_list = list()
    fh = open(fn)
    for line in fh:
        # line = line.rstrip()
        return_list.append(int(line))
    return return_list

prime_list = filetolist("primenumbers.txt")
happy_list = filetolist("happynumbers.txt")

print([elem for elem in prime_list if elem in happy_list])
