## Write a program to print a list after performing running sum on it.
list1 = [1,2,3,4,5,6]
sum = 0
result_list = []

for i in list1:
    sum += i
    result_list.append(sum)

print(result_list)


## You are given a list of integers. You are asked to make a list by running 
# through elements of the list by adding all elements greater and itself.
L = [2,4,6,10,1]
new_list = []

for i in L:
    add = 0
    for j in L:
        if j >= i:
            add += j
    new_list.append(add)

print(new_list)
