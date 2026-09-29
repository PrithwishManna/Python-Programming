### filter: selects some items (N inputs → ≤N outputs).

# numbers greater than 5


L = [2,6,9,3,12,4,5]

a = filter(lambda x: x > 5, L)

print(list(a))


# ____________________________________________


# fetch fruits starting with 'a'


fruits = ['apple', 'cherry', 'mango', 'watermelon', 'banana', 'pine-apple', 'avocado']

b = filter(lambda x: x.startswith('a'), fruits)

print(list(b))