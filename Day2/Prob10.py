# Print all the Armstrong numbers in a given range.

lower = int(input("Enter lower range: "))
upper = int(input("Enter lower range: "))

print(f"Armstrong numbers b\w {lower} and {upper} are:")

for num in range(lower, upper + 1):
    sum_cubes = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum_cubes += digit ** 3
        temp //= 10

    if num == sum_cubes:
        print(num)


# Importance of line 11 : When 'while' loop ends then num = 0, so if statement never run.