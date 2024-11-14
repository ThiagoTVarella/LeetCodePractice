from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        qu = deque()
        stack = [[]]
        layer = 0
        current_num = ''
        for ch in s:
            if ch.isdigit():
                current_num += ch
            elif ch == '[':
                num = int(current_num)
                current_num = ''
                layer += 1
                if len(stack) <= layer:
                    qu = deque()
                    stack.append(qu)
                stack[layer].append(num)
            elif ch.isalnum():
                stack[layer].append(ch)
            elif ch == ']':
                n = stack[layer].popleft()
                layer -= 1
                for i in range(n):
                    for j in range(len(stack[layer+1])):
                        elem = stack[layer+1][j]
                        stack[layer].append(elem)
                del stack[layer+1]

        ans = ''
        for elem in stack[0]:
            ans += elem

        return ans
                

# x3[a2[c]g3[f]]
# [[x],[3,a,c,c,g],[3, f]]
# layer = 2