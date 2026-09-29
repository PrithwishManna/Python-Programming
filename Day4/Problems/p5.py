# Sort a list of alphanumeric strings based on product value of numeric character in it. 
# If in any string there is no numeric character take it's product value as 1.

L = ['1ac21', '23fg', '456', '098d','1','kls']
sorted_L = []

for s in L:
    product = 1
    has_digit = False
    
    for char in s:
        if char.isdigit():
            product *= int(char)
            has_digit = True
    if not has_digit:
        product = 1
        
    sorted_L.append((product, s))               ## It packages the calculated score (product) and the original 
                                                # data (string) together into a Tuple and adds it to a list.
sorted_L.sort(reverse=True)                     ## When Python sorts a list of tuples, it always looks at the first item in the tuple first.
                                                # we force Python to sort based on the math value, not the string alphabet.
result = [item[1] for item in sorted_L]         ## This is a List Comprehension that extracts only the original strings 
                                                # from the list of pairs, discarding the calculated numbers.
print(result)