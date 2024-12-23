def isBalanced(s):
    # Function to check if the given string of brackets is balanced
    
    # Initialize an empty stack to keep track of opening brackets
    stack = []

    # Create a mapping of closing brackets to their corresponding opening brackets
    mapping = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the input string
    for brace in s:
        if brace in mapping.values():  # Check if the character is an opening bracket
            stack.append(brace)  # Push it onto the stack
        elif brace in mapping:  # Check if the character is a closing bracket
            # If the stack is empty or the top element doesn't match the expected opening bracket
            if not stack or stack.pop() != mapping[brace]:
                return "NO"  # Return "NO" if brackets are unbalanced
        else:
            # If the character is not a bracket, return "NO"
            return "NO"
    
    # If the stack is empty, all brackets are balanced; otherwise, they are not
    return "YES" if not stack else "NO"
