def RLE(text):
    if len(text) == 1:
        return '1'+text
    i = 0
    output = ''
    while i < len(text)-1:
        count = 1
        while i < len(text)-1 and text[i] == text[i+1]:
            count += 1
            i += 1
        output = output + str(count) + text[i]
        i += 1

    if text[-1] != text[-2]:
        output = output + str(1) + text[-1]

    
    return output


class Solution:
    def countAndSay(self, n: int) -> str:
        # Input is int, output is str

        if n == 1:
            return "1"

        def count_rec(n):
            # input int, output str
            if n == 1: return "1"
            return RLE(count_rec(n-1))

        return count_rec(n)