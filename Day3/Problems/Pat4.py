# Print the following pattern.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):        # Increasing part
    print("* " * i)

for i in range(rows - 1, 0, -1):    # Decreasing part
    print("* " * i)


"""
for i in range(-rows + 1, rows):
    print("* " * (rows - abs(i)))
"""