# Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.

input_str = input("Enter an alphanumeric string: ")

digits = [int(i) for i in input_str if i.isdigit()]
length = len(digits)
total_sum = 0

for i in range(length):
    total_sum += digits[i]

average = total_sum / length

print(f"sum: {total_sum}")
print(f"average: {average}")
