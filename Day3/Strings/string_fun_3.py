# split/ join

s = 'My name is Sonu'
print(s.split())                    # The .split() method is used to break a string into a list of substrings.
print('19-12-2025'.split('-'))

print(" ".join(['My', 'name', 'is', 'Sonu']))
print(" ".join([str(item) for item in ["Score:", 100]]))            # to convert numbers -> string


# strip

a = 'sonu               2003'           # Only removes whitespace from the start (leading) and the end (trailing) of a string.
print(a.strip())                        # Any spaces between characters (like the ones between 'sonu' and '2003') are left completely untouched.

b = print(a.split())                    # print(a.split(' '))


# To turn multiple spaces into a single space:
print(" ".join(a.split())) 
# Output: 'sonu 2003'