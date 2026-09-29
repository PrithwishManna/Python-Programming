# Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is 
# greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.

N = int(input("Enter an integer N : "))
sum = 0
num = 1

keep = True

while num <= N and keep:
    is_not_div_5 = (num % 5) != 0

    if is_not_div_5:
        total_sum = sum + num

        if total_sum <= 300:
            sum = total_sum
        else:
            print(f"\n--- Limit Reached ---")
            print(f"Adding {num} would exceed 300. Stopping.")
            keep = False

    if keep:
        num += 1


print(f"\nFinal Calculated Sum (<= 300): {sum}")
