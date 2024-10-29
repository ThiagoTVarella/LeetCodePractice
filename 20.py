def valid_parentheses(s: str) -> bool:
    # Create stack using list
    bracket_dict = {'(':')','[':']','{':'}'}

    stack = []
    
    # Iterate through s
    for char in s:
        
        # Check if opening brackets
        if char in '([{':
            stack.append(char)
        elif not stack:
            return False
        else:
            opening = stack.pop()
            if bracket_dict[opening] != char:
                return False
    
    if not stack:
        return True
    else:
        return False

print(valid_parentheses('()[]{}'))