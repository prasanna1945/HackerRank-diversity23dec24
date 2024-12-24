# Import the datetime module for working with dates
from datetime import datetime  

# Take two date inputs as strings in 'dd-mm-yyyy' format
d1 = input()  # Input first date
d2 = input()  # Input second date

try:
    # Parse the input strings into datetime objects using the specified format
    date1 = datetime.strptime(d1, "%d-%m-%Y")  # Convert first date string to datetime object
    date2 = datetime.strptime(d2, "%d-%m-%Y")  # Convert second date string to datetime object

    # Calculate the absolute difference between the two dates
    diff = abs(date1 - date2)  # 'abs()' ensures the result is always positive

    # Output the difference in days
    print(diff.days)  # Access the 'days' attribute to get the difference in days

except ValueError:
    # Handle errors caused by invalid date formats
    print("ERROR")  # Print error message if input date format is invalid
