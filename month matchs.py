def get_month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month_number >= 1 and month_number <= 12:
        return months[month_number - 1]
    else:
        return "Invalid month number"


month_number = int(input("Enter a number between 1 and 12: "))
print("Month:", get_month_name(month_number))

