num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
if num_1 <= num_2:
    print("Including the limits")
    for number in range(num_1, num_2 + 1):
        print(number)

print("Excluding the limits")
for number in range(num_1 + 1, num_2):
    print(number)

else: 
    print("The first number must be less than or equal to the second number.")
     