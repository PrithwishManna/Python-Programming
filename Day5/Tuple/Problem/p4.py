## Count no of tuples, list and set from a list

list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

list2 = []
set2 = []
tuple2 = []

for i in list1:
  if type(i) == list:
    list2.append(i)
  elif type(i) == set:
    set2.append(i)
  elif type(i) == tuple:
    tuple2.append(i)

print("List-", len(list2))
print("Set-", len(set2))
print("Tuples-", len(tuple2))