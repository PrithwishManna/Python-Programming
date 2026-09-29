# Write a program to print whether a given number is a prime number or not.

n = int(input("Enter a positive number: "))

if n <= 1:
    print(f"{n} is not a prime number")
elif n <= 3:
    print(f"{n} is a prime number")
else:
    is_prime = True
    N = n // 2
    
    for num in range(2, N + 1):
        if n % num == 0:
            is_prime = False
            break
            
    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
