## Check is tuples are same or not?
# Two tuples would be same if both tuples have same element at same index



t1 = (1, 2, 3, 0)
t2 = (0, 1, 2, 3)

# 1. First, check length. If lengths differ, they can't be the same.
if len(t1) != len(t2):
    luck = False
else:
    luck = True
    
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            luck = False
            break  # Found a mismatch, stop checking

if luck:
    print("Tuples are same")
else:
    print("Tuples are not same")