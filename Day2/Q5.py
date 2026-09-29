# 1. Investment Growth
"""
A person invests an initial amount of $5,000 in a savings account that offers an annual interest rate of 4%, compounded annually. 
Write a program to calculate the total amount of money in the account at the end of each of the next 5 years.
"""
pri_invest = 5000

for i in range(1, 6):
    print("In year", i, "investment is", pri_invest)
    pri_invest += 0.04 * pri_invest


# 2. Asset Depreciation
"""
A company buys a new machine for $25,000. The value of the machine is expected to depreciate (decrease) by 15% each year. 
Write a program to determine the value of the machine at the end of the after 8 years.
"""
price = 25000

for i in range(1, 9):
    price -= 0.15 * price

print("After 8 years price of the machine is :", price)


# 3. Bacteria Colony Growth
"""
A biology experiment starts with 1,000 bacteria in a petri dish. The colony's population is observed to increase at a rate of 20% every hour. 
Write a program to find the population of the bacteria colony at the end of the next 12 hours.
"""
number = 1000

for i in range(1, 13):
    number += 0.2 * number

print("After 12 hours population of the bacteria :", number)