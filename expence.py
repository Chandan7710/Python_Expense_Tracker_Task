'''
Expense Tracker:
The user should be able to enter the daily expenses, the expense should be stored 
in a file and loaded from the file, the expense should be totaled and show the daily, 
weekly and monthly total expenses.

Expense Information:
Date
Item
Rate

'''

import datetime
import time

date_list = []

today_date = input("Enter the the todays date : ")

day_items = int(input("Enter the number of items you need to purchase today :"))

item_list = []
rate_list = []

'''
Using for loop to loop through number of items in a day
and asking user input for item and price
'''

for i in range(day_items):
    item = input(f"Enter the {i+1} item you are purhasing on the day {today_date}:")
    item_list.append(item)
    rate = int(input(f"Enter the rate of the {i+1} item :"))
    rate_list.append(rate)

'''
Storing the item and the rate as a key value pair in a dictionary d1

'''
d1 = dict(zip(item_list, rate_list))
print(d1)


'''
Using Python file handling append function to append the 
date, item, price to the file name tracker.txt
'''


file = open("tracker.txt", "a+")
file.write(f"&&& Expences of the day {today_date} &&&\n\n")
file.write("$$$ The Items and Rates are $$$\n\n")


for x, y in d1.items():
    file.write(f"{x} - {y} \n")
file.write("\n")
file.close()
