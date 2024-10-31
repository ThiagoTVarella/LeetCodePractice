class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        exceptions = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        # Starting with the final value
        value = 0

        prev_char = s[0]
        i_char = 1
        
        while i_char < len(s):
            char = s[i_char]
            prev_value = roman_dict[prev_char]
            curr_value = roman_dict[char]

            # If not first and is exception:
            if prev_value < curr_value:
                curr_pair = prev_char + char
                value += exceptions[curr_pair]
                i_char += 1
                if i_char < len(s):
                    prev_char = s[i_char]

            # If not first and is normal:
            else:
                value += roman_dict[prev_char]
                prev_char = char

            i_char += 1

        if i_char == len(s):
            value += roman_dict[s[-1]]

        return value