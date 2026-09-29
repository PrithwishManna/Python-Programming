## Split String of list on K character.

L = ['IIT is a institution', 'for Technology and', 'science.']
K = ' '
output_list = []

for s in L:
    string = ""
    for char in s:
        if char == K:
            if string:
                output_list.append(string)
            string = ""
        else:
            string += char
    if string:
        output_list.append(string)

print(output_list)