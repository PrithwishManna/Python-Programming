## Write a list comprehension that can flatten a nested list

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

output = [j for i in matrix for j in i]
print(output)