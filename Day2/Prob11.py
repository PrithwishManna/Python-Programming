# Calculate the angle between the hour hand and minute hand.
# Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. 
# For example, if the final angle is 10.61, we need to print 10.


h = int(input("Enter Hour (1-12): "))
m = int(input("Enter Minutes (0-59): "))

# 12 o'clock is treated as 0 for calculation
if h == 12:
    h = 0

# Hour hand moves 30 deg per hour and 0.5 deg per minute
hour_pos = (h * 30) + (m * 0.5)

# Minute hand moves 6 deg per minute
min_pos = m * 6

angle = hour_pos - min_pos
if angle < 0:
    angle = -angle

# Get the smaller of the two possible angles
if angle > 180:
    angle = 360 - angle

# Print the floor (integer part)
print(int(angle))