## Write a program to add two lists index-wise. Create a new list that contains the 
# 0th index item from both the list, then the 1st index item, and so on till the last element.
# Any leftover items will get added at the end of the new list.

list1 = ["M", "na", "i", "so"]
list2 = ["y", "me", "s", "nu"]

L = [list(i) for i in zip(list1, list2)]                    # for list of list
print(L)

#zipped = zip(list1, list2)
#print(list(zipped))                                        # for list of tuples


## Write a program that can find the max number of each row of a matrix


l = [[1,2,3],[4,5,6],[7,8,9]]
lis = []

for i in l:
  lis.append(max(i))

print(lis)