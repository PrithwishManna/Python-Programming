# Write a program that will take a decimal number as input and prints out the binary equivalent of the number

num = float(input("Enter any number(decimal part: 0.5/ 0.25/ 0.75/ 0.125/ 0.625/ 0.3125/ 0.0625): "))

int_part = int(num)
binary_int = ""
if int_part == 0:
    binary_int = '0'
while int_part > 0:
    binary_int = str(int_part % 2) + binary_int
    int_part //= 2

frac_part = num - int(num)
binary_frac = ''

while frac_part > 0:                                                        # We limit to 10 places to avoid infinite loops
    frac_part *= 2
    bit = int(frac_part)
    binary_frac += str(bit)
    frac_part -= bit

print(binary_int + "." + binary_frac) 