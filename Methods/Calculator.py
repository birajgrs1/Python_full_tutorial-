# Define mathematical operations

def myAddition(x, y):
    print("Performing the addition operation...")
    return x + y

def mySubtraction(x, y):
    print("Performing the subtraction operation...")
    return x - y

def myMultiplication(x, y):
    print("Performing the multiplication operation...")
    return x * y

def myDivision(x, y):
    print("Performing the division operation...")
    if y != 0:
        return x / y
    else:
        return "Division by zero.\nMath Error!"

def myMenu():
    print("----------Main Menu----------")
    print("1. Addition Operation")
    print("2. Subtraction Operation")
    print("3. Multiplication Operation")
    print("4. Division Operation")

    try:
        ch = int(input("Please enter your option number: "))
        return ch
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        return None

def calculation():
    ch = myMenu()

    if ch is None or ch not in [1, 2, 3, 4]:
        print("Invalid choice!!!")
        return

    try:
        num1 = float(input("Enter any first number: "))
        num2 = float(input("Enter any second number: "))

        if ch == 1:
            result = myAddition(num1, num2)
        elif ch == 2:
            result = mySubtraction(num1, num2)
        elif ch == 3:
            result = myMultiplication(num1, num2)
        elif ch == 4:
            result = myDivision(num1, num2)

        print("Show Result: ", result)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

calculation()
