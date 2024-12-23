# Read the number of rows and columns from input
rows, cols = map(int, input().split())

# Initialize an empty list to store the input matrix
matrix = []

# Read the matrix row by row
for i in range(rows):
    # Append each row to the matrix after converting input to integers
    matrix.append(list(map(int, input().split())))

# Initialize an empty list for the transpose of the matrix
transpose = []

# Compute the transpose of the matrix
for i in range(cols):  # Iterate through columns
    trans_row = []  # Create a row for the transpose
    for j in range(rows):  # Iterate through rows
        trans_row.append(matrix[j][i])  # Add the element at (j, i) to the transposed row
    transpose.append(trans_row)  # Add the transposed row to the transpose matrix

# Initialize an empty list for the result matrix
res = []

# Compute the product of the matrix with its transpose
for i in range(rows):  # Iterate through rows of the original matrix
    res_row = []  # Create a row for the result matrix
    for j in range(rows):  # Iterate through rows of the transpose
        total = 0  # Initialize total for the dot product
        for k in range(cols):  # Compute the dot product of the row and column
            total += matrix[i][k] * transpose[k][j]
        res_row.append(total)  # Append the computed value to the result row
    res.append(res_row)  # Add the row to the result matrix

# Print the result matrix
for row in res:
    print(*row)  # Print each row with elements separated by spaces
