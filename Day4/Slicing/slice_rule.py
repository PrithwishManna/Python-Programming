"""
The full list slicing syntax is: [start:stop:step].
● start: The index where the slice begins (inclusive, default is 0).
● stop: The index where the slice ends (exclusive, default is the end of the list).
● step: The number of elements to skip between each selection (default is 1).
"""
my_list = [10, 8, 6, 4, 2]
new_list_step = my_list[::2]
print(new_list_step)

"""
The start and stop values are omitted, so the slice defaults to the entire list (from index 0 to the end).
"""

# Reverse slicing

L = [1,2,3,4,5]
print(L[::-1])