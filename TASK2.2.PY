

while True:
    print("\nCalculator")
    print("1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")

    choice = input("Select operation: ")

    if choice == "5":
        break

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", x + y)
    elif choice == "2":
        print("Result:", x - y)
    elif choice == "3":
        print("Result:", x * y)
    elif choice == "4":
        print("Result:", "Error" if y == 0 else x / y)
    else:
        print("Invalid selection.")
