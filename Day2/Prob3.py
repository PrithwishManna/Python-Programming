running = True

while running:
    print("""
    1. cm to ft
    2. km to miles
    3. USD to Inr
    4. exit
    """)

    choice = input("Enter any number between (1, 2, 3, 4):")

    if choice == '1':
        cm = float(input("Enter the value in cm: "))
        ft = cm / 30.48
        print("Your value in feet :", ft)
    elif choice == '2':
        km = float(input("Enter the value in km: "))
        miles = km * 0.621371
        print("Your value in miles :", miles)
    elif choice == '3':
        USD = float(input("Enter the value in USD: "))
        INR = USD * 90.41
        print("Your value in INR :", INR)
    elif choice == '4':
        print("exit")
        running = False
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
