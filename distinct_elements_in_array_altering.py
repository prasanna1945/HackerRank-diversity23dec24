# Read space-separated integers from input, convert them to a list of integers
arr = [int(i) for i in input().split()]

# Remove duplicates by converting the list to a set, then back to a list
s = list(set(arr))

# Initialize an empty list to store the output pattern
p = []

# Sort the list in ascending order
s.sort()

# Create a reversed version of the sorted list (descending order)
r = s[::-1]

# Initialize indices for traversing the sorted and reversed lists
sindex = 0  # Index for the sorted list
rindex = 0  # Index for the reversed list

# Loop through the range equal to the length of the list
for i in range(0, len(s)):
    if i % 2 == 0:  # For even indices, pick elements from the sorted list
        p.append(s[sindex])
        sindex += 1
    else:  # For odd indices, pick elements from the reversed list
        p.append(r[rindex])
        rindex += 1 

# Print the final pattern as a space-separated string
print(' '.join(map(str, p)))
