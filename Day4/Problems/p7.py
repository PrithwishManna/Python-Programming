## Add Space between Potential Words.

L = ['campusxIs', 'bestFor', 'dataScientist']
new_list = []

for string in L:
    str = ""
    for i in string:
        if i.isupper():
            str += ' ' 
            str += i       
        else:
            str += i
    new_list.append(str)

print(new_list)



## Write a program that can perform union operation on 2 lists

l1 = [1,2,3,4,5,1]
l2 = [2,3,5,7,8]

a = set(l1).union(set(l2))
print(list(a))
