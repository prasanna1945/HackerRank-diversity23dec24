def plusMinus(arr):
    # Function to calculate the ratio of positive, negative, and zero elements in the array
    
    # Find the total number of elements in the array
    n = len(arr)

    # Initialize counters for positive, negative, and zero elements
    oc = 0  # Counter for zeros
    pc = 0  # Counter for positive numbers
    nc = 0  # Counter for negative numbers

    # Iterate through each element in the array
    for i in arr:
        if i == 0:
            # Increment zero counter if element is 0
            oc += 1
        elif i < 0:
            # Increment negative counter if element is less than 0
            nc += 1
        else:
            # Increment positive counter for all other cases (positive numbers)
            pc += 1

    # Print the ratios of positive, negative, and zero elements
    print(pc / n)  # Ratio of positive numbers
    print(nc / n)  # Ratio of negative numbers
    print(oc / n)  # Ratio of zeros
