# Input the number of elements
n = int(input())

# Read the array elements and store them in a list
arr = [int(i) for i in input().split()]

# Sort the array in ascending order
arr.sort()

# Check if the number of elements is even
if n % 2 == 0:
    # Split the array into two halves
    arr1 = arr[0:n//2]  # First half
    arr2 = arr[n//2:n]  # Second half
    arr2 = arr2[::-1]   # Reverse the second half
else:
    # For odd number of elements, split accordingly
    arr1 = arr[0:(n//2)+1]  # First half including the middle element
    arr2 = arr[(n//2)+1:n]  # Second half
    arr2 = arr2[::-1]       # Reverse the second half

# Combine the two halves and print the result
print(' '.join(map(str, arr1 + arr2)))
