# type conversion
d = dict([('name','sonu'),('age',23),(4,3)])            # 'dict' convert 'list of tuples' => 'dictionary'
print(d)

# duplicate keys
dr = {'name':'sonu','name':'Prithwish'}                 # If dictionary have duplicate keys, then updated key will be output
print(dr)

d1 = {'name':'sonu',(1,2,3):6}
print(d1)


## Accessing items
# []
dv = {'name':'sonu','age':23,4:3}  
print(dv['name'])                                       # dictionary[keys] => values
# get
print(dv.get('age'))

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

print(data['subjects']['LA'])


## Adding key-value pair
dv['DOB'] = '25/06/2003'
print(dv)

## deleting
del data['subjects']['Programming C']
print(data)


