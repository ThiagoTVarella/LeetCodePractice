from typing import List

class Solution:
    def verticalOrder(self, root: List[int]) -> List[List[int]]:

        parent = lambda pos: (pos-1)//2

        # I want a hashmap that the keys are horizontal positions, and 
        # the values are the elements itself
        hash_horpos = {}

        # First, I'll create a list associating each element of root with its
        # horizontal position 
        hor_positions = [0]
        for i in range(1,len(root)):
            if i%2:
                hor_positions.append(hor_positions[parent(i)] - 1)
            else:
                hor_positions.append(hor_positions[parent(i)] + 1)

        # Then, I will go through each element of root, and store its horizontal
        # position in the hashmap. I will also keep track of the minimum and max
        minh = 1
        maxh = 0 
        for i,elem in enumerate(root):
            if elem is not None:
                horpos = hor_positions[i]
                if horpos < minh:
                    minh = horpos 
                elif horpos > maxh:
                    maxh = horpos

                if horpos in hash_horpos:
                    hash_horpos[horpos].append(elem)
                else:
                    hash_horpos[horpos] = [elem]

        # Then, I will iterate from minimum to max, and create the output list
        answer = []
        for i in range(minh,maxh+1):
            answer.append(hash_horpos[i])

        return answer 

Sol = Solution()
root = [1,2,3,4,10,9,11,None,5,None,None,None,None,None,None,None,None,None,6]
print(Sol.verticalOrder(root))





from collections import deque

left = lambda x: 2*x + 1
right = lambda x: 2*x + 2

def verticalOrder(root):
    pos = 0
    count = {}
    i = 0

    qu = deque()
    qu.append((0,pos))

    minp = 0
    maxp = 0

    countiii = 0

    while qu:
        node,pos = qu.popleft()
        if pos in count: 
            count[pos].append(root[node])
        else: 
            count[pos] = [root[node]]
        minp = min(minp,pos)
        maxp = max(maxp,pos)
        if left(node) < len(root) and root[left(node)] is not None:
            qu.append((left(node),pos-1))
        if right(node) < len(root) and root[right(node)] is not None:
            qu.append((right(node),pos+1))

    output = []

    for pos in range(minp,maxp+1):
        output.append(count[pos])

    return output

null = None
root = [3,9,20,null,null,15,7]
root = [3,9,8,4,0,1,7]

print(verticalOrder(root))