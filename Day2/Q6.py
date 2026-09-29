# 4. Car Value Depreciation
"""
A new car is purchased for $30,000. Its market value decreases by 12% in the first year and then by 8% in each subsequent year. 
Write a program to calculate the car's market value at the end of each of the next 6 years.
"""
price = 30000

for i in range(1, 7):
    if i == 1:
        price -= 0.12 * price
        print("In year", i, "value is :", price)
    else:
        price -= 0.08 * price
        print("In year", i, "value is :", price)


# 6. Radioactive Decay
"""
A sample of a substance currently contains 500 grams. Due to radioactive decay, the mass of the substance decreases by 5% every month. 
Write a program to calculate the remaining mass of the substance at the end of the next 6 months.
"""
weight =  500

for i in range(1, 7):
    weight -= 0.05 * weight

print("After 6 months weight :", weight)