hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter the number of hours worked: "))
weekly_hours = hours_worked * 5
part_time_hours = hours_worked / 2
weekly_pay = hourly_rate * (weekly_hours + part_time_hours)
print("Your weekly pay is:", weekly_pay)