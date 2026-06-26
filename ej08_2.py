number_1 = int(input("Enter first integer number: "))
number_2 = int(input("Enter second integer number: "))

print("Sum:", number_1 + number_2)
print("Subtract:", number_1 - number_2)
print("Multiply:", number_1 * number_2)

if number_2 == 0:
    print("You can't divide by zero.")
else:
    print("Divide:", number_1 / number_2)