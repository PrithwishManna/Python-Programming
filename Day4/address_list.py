# id() gives address of memory of variable
# Actually List contains address of memories where the value is saved


L = [1, 2, 3]

print(id(L))            # Address of list L

print(id(L[0]))         # Address of 1st element of list L
print(id(L[1]))         # Address of 1st element of list L
print(id(L[2]))         # Address of 1st element of list L

print(id(1))
print(id(2))
print(id(3))