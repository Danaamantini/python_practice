n = int(input("How many numbers do you want to display? "))

number = 1
count = 0

while count < n:

    if number % 3 == 0 and number % 5 != 0:
        print(number)
        count += 1

    number += 1
    