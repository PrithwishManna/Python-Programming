# Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

keep = True

sum = 0
count = 0

while keep:
    n = float(input("Enter a number : "))
    if n == 0:
        keep = False
    else:
        sum += n
        count += 1

final_sum = sum
print(final_sum)

if count > 0:
    average = final_sum / count
    print(f"Average: {average}")
else:
    print("No numbers were entered to calculated an average")
