width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
if width > 0 and height > 0:
    for row in range(height):
        print("x" * width)
    else: 
        print("Width and height must be positive integers.")   