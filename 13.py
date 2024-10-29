class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        exceptions = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        value = 0
        prev_val = roman_dict[s[0]]

        except_flag = False
        
        for character_i in range(1,len(s)):
            curr_val = roman_dict[s[character_i]]
            if curr_val <= prev_val or except_flag:
                value += prev_val
                prev_val = curr_val
                except_flag = False
            else:
                numeral = s[character_i-1]+s[character_i]
                value += exceptions[numeral]
                prev_val = 0
                except_flag = True
            print(value)
        if prev_val != 0:
            value += roman_dict[s[len(s)-1]]

        return value
