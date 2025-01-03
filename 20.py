class Solution:
    def isValid(self, s: str) -> bool:
        # # Create counters:
        # br_1 = 0 # for ()s
        # br_2 = 0 # for []s
        # br_3 = 0 # for {}s

        # stack = []

        # for char in s:
        #     if char in '([{':
        #         stack.append(char)
            
        #     if not stack:
        #         return False

        #     if char == ')':
        #         open_br = stack.pop()
        #         if open_br == '(':
        #             pass
        #         else:
        #             return False

        #     if char == ']':
        #         open_br = stack.pop()
        #         if open_br == '[':
        #             pass
        #         else:
        #             return False

        #     if char == '}':
        #         open_br = stack.pop()
        #         if open_br == '{':
        #             pass
        #         else:
        #             return False

        # if not stack:
        #     return True
        # else:
        #     return False

        # # for char in s:
        # #     if char == '(':
        # #         br_1 += 1
        # #     elif char == ')':
        # #         br_1 -= 1
        # #     elif char == '[':
        # #         br_2 += 1
        # #     elif char == ']':
        # #         br_2 -= 1
        # #     elif char == '{':
        # #         br_3 += 1
        # #     elif char == '}':
        # #         br_3 -= 1
        # #     else:
        # #         return False

        # #     if br_1 < 0 or br_2 < 0 or br_3 < 0:
        # #         return False

        # # if br_1 > 0 or br_2 > 0 or br_3 > 0:
        # #     return False
        # # else:
        # #     return True    

        stack = []
        opens = '({['
        closes = ')}]'
        dict_br = {'(':1,')':1,'{':2,'}':2,'[':3,']':3}

        for elem in s:
            if elem in opens:
                stack.append(dict_br[elem])
            elif elem in closes:
                if not stack:
                    return False
                check = stack.pop()
                if dict_br[elem] != check:
                    return False 
        if not stack:
            return True
        else:
            return False