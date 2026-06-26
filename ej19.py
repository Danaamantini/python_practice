number = int(input("Enter an integer number: "))
is_single_digit = number >= -9 and number <= 9
odd = number % 2 != 0
both = is_single_digit and odd
neither = not is_single_digit and not odd
print ("single digit:", is_single_digit)
print ("odd:", odd)
print ("both:", both)
print ("neither:", neither)