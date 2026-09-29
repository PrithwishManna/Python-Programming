## Write a list comprehension to print the following matrix
##[[0, 1, 2], [3, 4, 5], [6, 7, 8]]

matrix = [[j for j in range(i * 3, (1 + i) * 3)] for i in range(3)]
print(matrix)





## Write a list comprehension that can transpose a given matrix

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

for row in transpose:
    print(row)
