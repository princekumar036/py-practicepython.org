'''
https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
Exercise 13 - Fibonacci 
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the
sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''
def fibonnaci(a):
    if a == 0:
        series = []
    elif a == 1:
        series = [1]
    else:
        i = 0
        series = [1, 1]
        while (i <= a-3):
            series.append(series[i]+series[i+1])
            i += 1
    return series