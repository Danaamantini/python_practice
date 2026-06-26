seats_available = int(input("Enter the number of available seats: "))
people_attending = int(input("Enter the number of people attending: "))
if people_attending <= seats_available:
    print("There are enough seats available.")
else: 
    missing_seats = people_attending - seats_available
    print("There are not enough seats available. You need", missing_seats, "more seats.")