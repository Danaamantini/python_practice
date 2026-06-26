num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 == num2:
    print("The first number is equal to the second number.")
if num1 > num2:
    if num1 % num2 == 0:
        print("The first number is greater than the second number and is divisible by it.")
    else:
        print("The first number is greater than the second number but is not divisible by it.")
if num1 < num2:
    if num2 % num1 == 0:
        print("The second number is greater than the first number and is divisible by it.")
    else:
        print("The second number is greater than the first number but is not divisible by it.")