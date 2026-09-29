## Adding items to a list

# append
L = [1, 2, 4, 7, 0]
L.append(True)                                      # append method provide the argument in the last of the list
print(L)

# extend
M = [0, 7, 4, 2, 1]
M.extend([2.3, 6 + 3j, True, 'Sonu'])               # extend method is used to add multiple elements to the end of an existing list.
print(M)

N = [1,2,3,4]
N.extend('Sonu')
print(N)

L.append([2.3, 6 + 3j, 'Sonu'])
print(L)


# insert

num = [111, 7, 2, 1]
num.insert(2,14)                                    # insert method first is location, second is the element
print(num)