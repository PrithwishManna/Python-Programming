list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2, list_1, sep="\n")

#It(slice) actually copies the list's contents, not the list's name.
#A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.

"""
my_list[start:end]
As you can see, it resembles indexing, but the colon inside makes a big difference.
A slice of this form makes a new (target) list, taking elements from the source list ‒ the elements of the indices from start to end - 1.
Note: not to end but to end - 1. An element with an index equal to end is the first element which does not take part in the slicing.
Using negative values for both start and end is possible (just like in indexing).
"""