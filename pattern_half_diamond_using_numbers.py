# Read input values, split them, and convert to integers
arr = [int(i) for i in input().split()]  

# Assign the first value to 'm' and the second value to 'n'
m = arr[0]  # Starting number to print
n = arr[1]  # Number of rows for the pattern

# Generate the upper triangle of the pattern
for i in range(n):  # Loop for rows in the upper triangle
    for j in range(i + 1):  # Loop for columns in each row
        print(m, end="")  # Print 'm' without a newline
    print("")  # Move to the next line after each row
    m += 1  # Increment 'm' for the next row

# Adjust 'm' for the lower triangle
m -= 2  # Reset 'm' to the appropriate value for descending pattern

# Generate the lower triangle of the pattern
for i in range(n - 1):  # Loop for rows in the lower triangle
    for j in range(n, i + 1, -1):  # Loop for columns in each row
        print(m, end="")  # Print 'm' without a newline
    print("")  # Move to the next line after each row
    m -= 1  # Decrement 'm' for the next row
