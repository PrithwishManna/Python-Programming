n = range(4)
 
for num in n:
    print(num - 1)
else:
    print(num)

"""
else: In Python, a for...else construct means the code in the else block is executed only if the loop completes all its iterations without being terminated by a break statement. Since there is no break here, the else block will run.
print(num): When the loop finishes, the variable num retains the value from the last iteration, which was 3.

n = 0, 1, 2, 3
This line prints the final value of num, which is 3.
"""