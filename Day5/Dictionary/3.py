## Remove key-value pair
# pop
dv = {'name':'sonu','age':23,4:3,'school':'CHS','college':'IITG'}
dv.pop(4)
print(dv)                       # delete the provided key-value pair

# popitem
dv.popitem()                    # remove last key-value pair
print(dv)

# delete
del dv['age']
print(dv)

# clear
dv.clear()
print(dv)

data = {
    'name':'sonu',
    'collage':'IITG',
    'sem':1,
    'subjects':{
        'M Algebra':8,
        'LA':7,
        'Real':6,
        'Discrete':6,
        'Programming C':5
    }
}

data['subjects']['ring'] = 72
print(data)
