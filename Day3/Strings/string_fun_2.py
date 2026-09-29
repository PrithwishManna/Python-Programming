# endswith/ startswith
p = 'my name is sonu'
print(p.endswith('nu'))

print(p.startswith('my'))


# Format
name = 'Sonu'
sex = 'male'

s = 'Hi my name is {} and I am a {}'
u = s.format(name, sex)
print(u)

n = 'Hi my name is {1} and I am a {0}'.format(sex, name)
print(n)


# isalnum/ isalpha/ isdigit/ isidentifier/ isspace/ replace
print('sonu2003'.isalnum())         # It checks if a string contains only letters (A-Z) and numbers (0-9).
print('sonu@2003'.isalnum())        # This string contains the @ symbol. In Python's string methods, symbols, punctuation, and even spaces are not considered alphanumeric.

print('sonu'.isalpha())             # Only letters (no numbers/spaces/symbols).

print('2003'.isdigit())             # Only numbers (no letters/spaces/symbols).

print('1_first'.isidentifier())
print('first_1'.isidentifier())

print('so nu'.isspace())            # Only whitespace (spaces, tabs, newlines).

print('sonu@2003'.replace('@', ' '))