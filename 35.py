'''
https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html
35 - Birthday Months
In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
'''
import json
with open("scientistbdays.json" as f):
    