def minimum_add(s:str)->int:
    """
    Given string s of parenthesis, return the minimum number of parenthesis
    that should be added to make s valid

    E.g. if s = ((()((), then there are 3 ) missing so output is 3
    E.g. if s = ))(, then there are 2 ( missing and one ), so output is 3

    Time complexity: O(n)
    Space complexity: O(1)
    """
    # Handle edge cases
    if not s:
        return 0

    # Create missing_open counter
    # Create missing_close counter
    missing_close = missing_open = 0

    # Iterate over s
    for ch in s:

        # If ( found, add to missing_close counter
        if ch == '(': missing_close += 1 
        # If ) found and if missing_close is 0 add to missing_open counter
        elif ch == ')' and missing_close > 0: missing_close -= 1
        # If ) found and missing_close is not 0, remove from missing_close counter
        elif ch == ')': missing_open += 1
        # Handle faulty input gracefully
        else: return -1

    # Return missing counter + stack counter
    return missing_close + missing_open 

s = '(()'
s = '))('

print(minimum_add(s))