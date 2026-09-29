## Editing items in a List
L= [1,2,3,4,0]
L[-1] = 100                 # editing with indexing

L[1:4] = [200,300,400]      # editing with slicing
print(L)


## Deleting items from a List

# del                       # del L => it gives error
del L[-1]
del L[1:3]
print(L)

# remove
N = [1,5,2,3,4,5]
N.remove(5)                 # remove method searches for the first occurrence of the specific value you provide
print(N)

# pop
M = [1,2,3,4,5]
M.pop(1)                    # With an index: If you provide an index, like .pop(1), it removes the item at that specific position.
M.pop()                     # By default: If you don't provide a number, pop() removes the last item in the list.
print(M)

# clear
P = [1, 2, 3, 4, 'Sonu']
P.clear()                   # clear(), the list itself continues to exist in your computer's memory, but its contents are deleted
print(P) 


## The primary difference is that .clear() empties the container but keeps it alive, while del removes the name (variable) or specific slices from memory.
## del N (Whole variable): This deletes the variable name N entirely. If you try to print N afterward, you will get a NameError
