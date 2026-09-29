x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one")

if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")

"""
Because this if is not connected to the previous one, the elif and else belong only to this second if.

Since the if is True, Python skips the elif and else entirely.
"""