# Take two date inputs as strings from the user
d1 = input()
d2 = input()

# Import the datetime module to work with date and time
from datetime import datetime

try:
    # Parse the input strings into datetime objects with the given format (DD-MM-YYYY)
    date1 = datetime.strptime(d1, "%d-%m-%Y")
    date2 = datetime.strptime(d2, "%d-%m-%Y")

    # Compare the two dates
    if date1 == date2:
        # Print "Equal" if the dates are the same
        print("Equal")
    elif date1 < date2:
        # Print "Second" if the second date is later
        print("Second")
    else:
        # Print "First" if the first date is later
        print("First")

# Handle invalid date formats by catching ValueError
except ValueError:
    print("Error")

