# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.
keep = True

for i in range(2000, 3201):
    is_div_7 = (i % 7) == 0
    is_not_div_5 = (i % 5) != 0

    if is_div_7 and is_not_div_5:
        if not keep:
            print(",", end="")
        
        print(i, end="")
        keep = False

print("\n")
print("The even numbers b\w 1000 and 3000", "\n")

# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. 
# The numbers obtained should be printed in a space-separated sequence on a single line.

for num in range(1000, 3001):
    is_even = (num % 2) == 0

    if is_even:
        print(num, end=" ")