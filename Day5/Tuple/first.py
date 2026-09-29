t1 = ()
print(t1)

## Tuples are immutable

# create a tuple with a single item (unique)
t2 = (1,)
print(t2)                           # If t2 = (1)
print(type(t2))                     # type(t2) = int

# homo
t3 = (1,2,3,4,6)
print(t3)

#hetro
t4 = (1,2.5,True,[2,9,0,1],'sonu')
print(t4)

#nested tuple
t5 =(1,2,6,(5,3,8))
print(t5)

#using type conversion
t6 = tuple('hello')                 # In Python, a string is considered a sequence of characters.
print(t6)

# In tuples we can't 'adding','editation','delete'
# But we can delete the whole tuple