# Arithmetic Operations(+ , *)

print('delhi' + 'west')
print('sonu' * 3)
print('*' * 30)

# Relational Operations(< , <=, >, >=, ==, !=)

print('west' != 'West')
print('east' == 'sonu')
print('ghatal' > 'sonakhali')  # ascii value(s > g)
print('West' < 'west')         # ascii value(w > W)


# Conditional Operations('empty strings'-> False)

print('hasi' and 'khusi')   # The and operator looks for the first "falsy" value.If the first value is truthy (like 'hasi'), it moves on and returns the second value, regardless of whether it's truthy or falsy.
print('hasi' or 'khusi')    # The or operator looks for the first "truthy" value.Since 'hasi' is truthy, Python "short-circuits" (stops immediately) and returns 'hasi' without even looking at the second string.
print('' and 'sonu')        # As mentioned, and returns the first value if it is falsy.Since '' (an empty string) is considered falsy, Python returns it immediately and stops.
print(not '')

# Loop Operation

for i in 'west':
    print(i)

for i in 'west':
    print('sonu')

print('s' in 'sonu')
print('o' not in 'sonu')


