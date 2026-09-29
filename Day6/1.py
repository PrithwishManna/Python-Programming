def is_even(num):
    """
    This function detects the input is odd or even
    input: any valid integer
    output: odd/even
    MFG:20/01/2026
    """
    if type(num) == int:
        if num % 2 == 0:
            return 'even'
        else:
            return 'odd'
    else:
        return 'Give input in integer'
    
print(is_even('hi'))    
#for i in range(1,6):
#    x = is_even(i)
#    print(x)

    