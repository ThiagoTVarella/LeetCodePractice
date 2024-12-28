class Solution:
    def isNumber(self, s: str) -> bool:
        
        # Integer = -/+ and digits [and exponent]
        # decimal = -/+ [digits].[digits] [and exponent]
        # exponent = e/E and Integer

        # first ch must be -,+,or digit
        # if isalpha(), needs to be e or E, and just once
        # after e can have + or - again.

        # check if first is digit
        # if not, check if it is not -+.

        if s == '.':
            return False

        n = len(s)
        i = 0

        seen_digit = False
        seen_exp = False
        seen_dec = False

        while i < n:
            if s[i].isdigit():
                seen_digit = True
            elif s[i] in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
                if i == n-1:
                    return False
            elif s[i] in 'eE':
                if seen_exp or not seen_digit:
                    return False
                else:
                    if i == n-1:
                        return False
                    seen_exp = True
                    seen_digit = False
            elif s[i] == '.':
                if seen_dec or seen_exp:
                    return False
                seen_dec = True
            else:
                return False
            i += 1            
        
        return seen_digit

