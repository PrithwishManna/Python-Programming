def f():
    def x(a, b):
        return a + b
    return x                            ## f returns the function object x
                                        ## At this exact moment, the code effectively becomes: val = x(3, 4).
val = f()(3, 4)                         ## f()(3, 4) -> x(3, 4)
print(val)