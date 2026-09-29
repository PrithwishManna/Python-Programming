# In Python, the pass statement is a null operation. When it executes, nothing happens. 
# It is used as a placeholder in situations where the Python syntax requires a statement, but you don't have any action to perform yet.
# Think of it as a "Coming Soon" sign for your code.


for letter in "Python":
    if letter == "h":
        pass  # Just a placeholder
        print("This is the pass block")
    print("Current letter:", letter)
