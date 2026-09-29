## Find list of common unique items from two list. and show in increasing order

num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
new_list = []                               #list1 = []
                                            #for i in num1:
for i in num1:                              #    if i in num2:
  for j in num2:                            #        list1.append(i)
    if i == j:                              #    list1.sort()
      new_list.append(i)                    #print(list1)
  new_list.sort()
print(new_list)                                            
                                            


   
                                           
## Convert Character Matrix to single String using string comprehension.

L = [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]

output = ' '.join(["".join(string) for string in L])
print(output)                                            
