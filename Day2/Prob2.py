angle_1 = float(input("Enter first angle : "))
print(angle_1)

angle_2 = float(input("Enter second angle : "))
print(angle_2)

angle_3 = float(input("Enter third angle : "))
print(angle_3)

total = angle_1 + angle_2 + angle_3

is_positive = (angle_1 > 0) and (angle_2 > 0) and (angle_3 > 0)

is_180 = total == 180

if is_positive and is_180:
    print("Yes, these angles can form a triangle!")
else:
    print('No, these angles can\'t form a triangle')