class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        point = 1
        ans = ''
        base = ord('0')

        l1 = len(num1)
        l2 = len(num2)

        minlen = min(l1,l2)

        carry = 0

        while point <= minlen:

            add = carry + ord(num1[l1-point]) + ord(num2[l2-point]) - 2*base

            ans = str(add%10) + ans
            if add >= 10:
                carry = 1
            else:
                carry = 0

            point += 1
        
        if l1 < l2:
            while point <= l2:
                add = carry + ord(num2[l2-point]) - base

                ans = str(add%10) + ans
                
                if add >= 10:
                    carry = 1
                else:
                    carry = 0


                point += 1
        elif l2 < l1:
            while point <= l1:
                add = carry + ord(num1[l1-point]) - base

                ans = str(add%10) + ans
                
                if add >= 10:
                    carry = 1
                else:
                    carry = 0

                point += 1

        if carry == 1:
            ans = '1' + ans

        return ans

