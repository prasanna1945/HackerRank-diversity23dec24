# Initialize an empty list to store input numbers
arr = []

# Take space-separated input, split it into individual elements, and process each element
for i in input().split():
    # Check if the current number is -1; if yes, break the loop
    if int(i) == -1:
        break
    else:
        # Otherwise, convert the input to an integer and append it to the list
        arr.append(int(i))

# Create a set from the list to remove duplicates and convert it back to a list
s = list(set(arr))

# Sort the list in ascending order
s.sort()

# Print the second largest number in the list
print(s[len(s)-2])  
