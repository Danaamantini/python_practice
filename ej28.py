sum_of_ages = 0
count = 0

for person in range(5):
    age = int(input("Enter an age: "))

    sum_of_ages += age

    if age > 18 and age % 2 != 0:
        count += 1

average_age = sum_of_ages / 5

print("Average age:", average_age)
print("Adults over 18 with odd ages:", count)