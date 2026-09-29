### Write a program to add item 7000 after 6000 in the following Python List

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)


## Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]

for i, j in zip(candy_list, no_of_items):
    print(f"{i}-{j}")