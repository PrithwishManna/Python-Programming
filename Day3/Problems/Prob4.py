# Write a program to print all the unique combinations of 1,2,3 and 4

numbers = [1, 2, 3, 4]

for a in numbers:
    for b in numbers:
        for c in numbers:
            for d in numbers:
                if a != b and a != c and a != d and b != c and b != d and c != d:
                    print(a, b, c, d)
                    

