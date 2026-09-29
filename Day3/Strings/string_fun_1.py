# capitalize/ title/ upper/ lower/ swapcase

s = 'west bengal'
u = s.capitalize()
print(u)                # If I print s then nothing will be changed because 'strings' are immutable. So I create new string u.

v = s.title()
print(v)

w = s.upper()
print(w)

x = w.lower()
print(x)

y = 'wESt beNgAL'
z = y.swapcase()
print(z)


# count/ find/ index

a = 'west bengal'
print(a.count('e'))

p = 'my name is sonu'
print(p.find('is'))
print(p.find('z'))      # In find() if the substring DNE in main sting then it gives output => -1

print(p.index('n'))     # In index() if the substring DNE in main string then it gives outout => error
