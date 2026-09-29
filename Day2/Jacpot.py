# Jacpot game create

import random
jackpot = random.randint(1, 100)

guess = int(input("Guess a number : "))
count = 1

while guess != jackpot:
    if guess < jackpot:
        print('Guess a higher number')
    else:
        print('Guess a lower number')

    guess = int(input("Guess a number : "))
    count += 1

else:
    print('You own the Jackpot!!')
    print('Total attempt :', count)