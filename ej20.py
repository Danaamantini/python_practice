number_1 = int(input("Enter first integer number: "))
number_2 = int(input("Enter second integer number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    print("Sum:", number_1 + number_2)
elif operation == "-":
    print("Subtract:", number_1 - number_2)
elif operation == "*":
    print("Multiply:", number_1 * number_2)
elif operation == "/":
    if number_2 == 0:
        print("You can't divide by zero.")
    else:
        print("Divide:", number_1 / number_2)
else:
    print("Invalid operation.")