# Print the following pattern.

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for x in range(rows - i):     # For front spaces
        print(" ", end="")
    
    for j in range(1, i + 1):     # Increasing part
        print("* ", end="")
    print()

for i in range(rows - 1, 0, -1):
    for y in range(rows - i):     # For front spaces
        print(" ", end="")

    for k in range(i, 0, -1):     # Decreasing part
        print("* ", end="")
    print()