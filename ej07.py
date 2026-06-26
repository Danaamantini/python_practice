price_per_m2 = float(input("Enter the price per m2: ")) 

lot_width = float(input("Enter the width of your lot: ")) 

lot_length = float(input("Enter the length of your lot: "))

lot_m2 = lot_width * lot_length
perimeter = (lot_width + lot_length) * 2
wire_perimeter = perimeter * 3
lot_price = lot_m2 * price_per_m2
print ("The wire needed for the lot is:", wire_perimeter)
print ("The price of the lot is:", lot_price)
