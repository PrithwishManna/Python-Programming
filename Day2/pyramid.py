blocks = int(input("Enter the number of blocks: "))

height = 0

layer_blocks = 1
while blocks >= layer_blocks:
    
    blocks -= layer_blocks
    
    height += 1
    
    layer_blocks += 1

print("The height of the pyramid:", height)