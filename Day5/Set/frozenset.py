# frozen set is just an immutable version of a python set object
fs = frozenset([1,6,3,4])               # list/tuple/set
print(fs)

rs = frozenset({3,4,5,8})
print(fs | rs)

# works => all read functions
# doesn't work => write operations

# 2D set
gs = frozenset([2,3,6,frozenset({5,2,10})])
print(gs)

# set comprehension
print({i for i in range(1,11)})