number_1 = int(input("Enter first integer number: "))
number_2 = int(input("Enter second integer number: "))
number_3 = int(input("Enter third integer number: "))
if number_1 > number_2 and number_1 > number_3:
    print("The first number is the greatest.")
elif number_2 > number_1 and number_2 > number_3:
    print("The second number is the greatest.")
else:
    print("The third number is the greatest.")