dict = {'name':'sonu','age':23,'sex':'male'}            # key => name; value => sonu
# Characteristics:
#                 Mutable
#                 Indexing has no meaning
#                 key's can't be duplicate
#                 key's can't be mutable items

# empty dictionary
d = {}
print(d)
# 1D dictionary
dict1 = {'name':'sonu','sex':'male'}
print(dict1)
# mixed keys
di = {(1,2,4):1,'hello':'world'}
print(di)
# 2D dictionary
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
print(data)
