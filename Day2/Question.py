
# 7. Website Traffic Growth
"""
A new website currently receives 500 unique visitors per day. The marketing team aims for a growth rate of 5% per week. 
Write a program to determine the estimated daily unique visitors at the end of the after 10 weeks.
"""
day = 500
visitors = 7 * day

for i in range(1, 11):
    visitors += 0.05 * visitors

print("After 10 weeks total visitors :", visitors)

# 10. Salary Increase
"""
An employee's starting annual salary is $60,000. They are guaranteed an annual raise of 3% every year. 
Write a program to calculate the employee's annual salary at the end of each of the next 10 years.
"""
salary = 60000

for i in range(1, 11):
    print("In year", i, "salary is :", salary)
    salary += 0.03 * salary
