print("select the operation")
print(" 1 for Addition \n 2 for Subtraction\n 3 for Multiplication \n 4 for Division")
operation = input("enter the operation")
if operation == "1":
    num1 = input("enter first no:")
    num2 = input("enter second no.")
    if num1 == "56" and num2 == "9" or num1 =="9" and num2 =="56":
        print("the sum is 77")
    else:print("the sum is" + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("enter first no.")
    num2 = input("enter second no.")
    print("the difference is" + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("enter first no.")
    num2 = input("enter second no.")
    if num1 == "45" and num2 == "3" or num1 =="3" and num2 =="45":
        print("the product is 555")
    else:print("the product is" + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input(" enter first no.")
    num2 = input("enter second no.")
    if num1 == "56" and num2 == "4" or num1 =="4" and num2 =="56":
        print("the result is 4")
    else:print("the result is" + str(int(num1) / int(num2)))
else: "invalid entry"