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