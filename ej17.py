age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
if age >= 1 and age <= 120:
    print("Valid age for retirement.")
    if gender == "M": 
        if age >= 65:
            print("You are eligible for retirement.")
        else:
            print("You are not eligible for retirement.")
    elif gender == "F":
        if age >= 60:
            print("You are eligible for retirement.")
        else:
            print("You are not eligible for retirement.")
            