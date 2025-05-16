def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = '/'
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid input.")
        return

    print(f"Result: {num1} {operation} {num2} = {result}")

# Run the calculator
calculator()
