# Nested if with List Comprehension
# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

K1 = [i for i in my_fruits if i in basket and i.startswith('a')]
print(K1)

K2 = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
print(K2)


# Print a 3x3 matrix using list coprehension -> Nested List comprehension

M = [[i * j for i in range(1, 4)] for j in range(1, 4)]
print(M)


# cartesian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]

L = [i * j for i in L1 for j in L2]
print(L)
