class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        
        # Pointers
        pt1 = len(num1)-1
        pt2 = len(num2)-1

        # Auxiliary variables
        k = 0
        carry = 0

        # Output
        final = ''

        while k <= max(pt1,pt2):

            # If k smaller than both nums, add digs. Otherwise, pick the bigger num
            if k <= min(pt1,pt2): 
                dig = int(num1[pt1-k])+int(num2[pt2-k])
            else: 
                dig = int(num1[pt1-k]) if pt1>=pt2 else int(num2[pt2-k])

            # Realize sum operation
            soma = dig+carry
            new_final_digit,carry = soma%10,soma//10

            # Store digit and iterate
            final = str(new_final_digit) + final
            k += 1

        if carry == 1: return '1'+final
        else: return final

















        # point = 1
        # ans = ''
        # base = ord('0')

        # l1 = len(num1)
        # l2 = len(num2)

        # minlen = min(l1,l2)

        # carry = 0

        # while point <= minlen:

        #     add = carry + ord(num1[l1-point]) + ord(num2[l2-point]) - 2*base

        #     ans = str(add%10) + ans
        #     if add >= 10:
        #         carry = 1
        #     else:
        #         carry = 0

        #     point += 1
        
        # if l1 < l2:
        #     while point <= l2:
        #         add = carry + ord(num2[l2-point]) - base

        #         ans = str(add%10) + ans
                
        #         if add >= 10:
        #             carry = 1
        #         else:
        #             carry = 0


        #         point += 1
        # elif l2 < l1:
        #     while point <= l1:
        #         add = carry + ord(num1[l1-point]) - base

        #         ans = str(add%10) + ans
                
        #         if add >= 10:
        #             carry = 1
        #         else:
        #             carry = 0

        #         point += 1

        # if carry == 1:
        #     ans = '1' + ans

        # return ans

