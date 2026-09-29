"""Write a program that will give you in hand 
monthly salary after deduction on CTC - HRA(10%), 
DA(5%), PF(3%) and taxes deduction as below:

Salary(Lakhs) : Tax(%)
Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%
"""
ctc_lakhs = float(input("Enter your salary in CTC(lakhs) : "))

annoual_income = ctc_lakhs * 100000

HRA_deduction = annoual_income * 0.1
DA_deduction = annoual_income * 0.05
PF_deduction = annoual_income * 0.03

print("HRA_deduction :", HRA_deduction)
print("DA_deduction :", DA_deduction)
print("PF_deduction :", PF_deduction)

total_deduction = HRA_deduction + DA_deduction + PF_deduction
Taxable_income = annoual_income - total_deduction
Taxable_income_lakh = Taxable_income / 100000

print("total_deduction :", total_deduction)
print("Taxable_income :", Taxable_income)
print("Taxable_income_lakh :", Taxable_income_lakh)

if Taxable_income_lakh < 5:
    Tax = 0
elif 5 <= Taxable_income_lakh < 10:
    Tax = 0.1
elif 10 <= Taxable_income_lakh < 20:
    Tax = 0.2
else:
    Tax = 0.3

print("Tax :", Tax)

annual_income_tax = Taxable_income * Tax
net_annual_income = Taxable_income - annual_income_tax

print("annual_income_tax :", annual_income_tax)
print("net_annual_income :", net_annual_income)

monthly_in_hand_salary = net_annual_income / 12

print("monthly_in_hand_salary :", monthly_in_hand_salary)