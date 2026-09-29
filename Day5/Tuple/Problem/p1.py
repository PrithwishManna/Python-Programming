## Join Tuples if similar initial element
# While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 

result_dict = {}

for key, val in test_list:
    if key in result_dict:
        result_dict[key].append(val)
    else:
        result_dict[key] = [val]

output = [tuple([key] + val_list) for key, val_list in result_dict.items()]

print('Joined Tuples:', output)