## Membership/ iteration

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

print('sem' in data)

d = {'name':'sonu', 'age':23, 'gender':'male'}
for i in d:
    print(i, d[i])                                      ## i => keys; d[i] => values

## Functions
# len/sorted
print(len(d))
print(max(d))                                           ## By ascii value 
print(min(d))
print(sorted(d))
print(sorted(d, reverse=True))

# items/keys/values
print(d.items())                            ## items(): dictionary => List of Tuples
print(d.keys())                             ## keys(): print all dictionary keys 
print(d.values())                           ## values(): print all dictionary values


a1 = {1:2, 4:6, 7:3}
b1 ={7:4, 3:5}
a1.update(b1)
print(a1)

# Dictionary Comprehension
    # Print first 10 numbers and their squares 
m = {i:i**2 for i in range(1,11)}
print(m)
    # Using existing dictionary
units_in_kg = {'rice':5,'dal':2,'fish':1.5,'vegies':3}
units_in_gm = {key:value * 1000 for (key,value) in units_in_kg.items()}
print(units_in_gm)
    # Using zip
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]        ## If we use curly bracess in position of Square bracess
temp_c = [28.2,26.3,29.5,30.3,31.9,33,28.7]                                            ## then the ans becomes randomly
weekly_weather = {i:j for (i,j) in zip(days,temp_c)}
print(weekly_weather)
    # using if condion
products = {'Phone':10,'Charger':0,'Laptop':4,'Tablet':0}
stock = {i:j for (i,j) in products.items() if j > 0}
print(stock)
# Nested comprehension
    # print tables of numbers from 2 to 4
table = {i:{j:j*i for j in range(1,11)} for i in range(2,5)}
print(table)