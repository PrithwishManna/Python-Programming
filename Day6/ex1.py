def g(x):
    def h(x):
        x = x + 1
        print('In h(x): x =', x)                ## here 'return x' nei tay next line aa abar x = 4 hobe
    x += 1
    print('In g(x): x =', x)
    h(x)
    return x

x = 3
z = g(x)

print('In main program scope: x = ', x)
print('In main program scope: z = ', z)