class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Define list with position of open brackets
        list_of_pos = []
        # Create list of chars
        list_of_chars = []
        
        # Iterate through string
        for elem in s:

            # Check if not isalnum()
            if not elem.isalnum():

                # Check if opening or closing
                if elem == '(':
                    
                    # If opening, remember position and add to list of chars
                    list_of_pos.append(len(list_of_chars))
                    list_of_chars.append('(')

                else:

                    # If closing, try to pop from list of chars
                    if list_of_pos:
                        list_of_pos.pop()
                        # If it can, include in list of chars
                        list_of_chars.append(')')
                    # If it can't pop, it just won't go to the list of chars

            # if is alnum put in list of chars
            else:
                list_of_chars.append(elem)

        # if list of positions is not empty, find position and pop from list of chars
        for pos in list_of_pos[::-1]:
            list_of_chars.pop(pos)

        # return string from list of chars
        return ''.join(list_of_chars)

class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:

#         keeps = []
#         stack_pos = []

#         for i,char in enumerate(s):
#             if char.isalnum():
#                 keeps.append(1)
#             elif char == '(':
#                 stack_pos.append(i)
#                 keeps.append(-1)
#             elif char == ')':
#                 if stack_pos:
#                     ind = stack_pos.pop()
#                     keeps[ind] = 1
#                     keeps.append(1)
#                 else:
#                     keeps.append(0)
        
#         while stack_pos:
#             ind = stack_pos.pop()
#             keeps[ind] = 0
        
#         ans = ''
#         for i,keep in enumerate(keeps):
#             if keep:
#                 ans += s[i]
        
#         return ans


