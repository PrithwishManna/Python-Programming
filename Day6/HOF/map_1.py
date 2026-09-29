### map: transforms every item (N inputs → N outputs).

# odd / even labeling of list items
L = [1,2,3,6,5,7,4,9]
a = map(lambda x: 'even' if x % 2 == 0 else 'odd', L)
print(list(a))

# fetch names from a list of dictionary

users = [
    {
        'name':'Rahul',
        'age': 45,
        'gender':'male'
    },
    {
        'name':'Pradip',
        'age':26,
        'gender':'male'
    },
    {
        'name':'Anindita',
        'age':24,
        'gender':'female'
    }
]

name = map(lambda users: users['name'], users)
print(list(name))