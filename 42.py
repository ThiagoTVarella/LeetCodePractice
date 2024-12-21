# def create_grid(height):
#     m = max(height)
#     grid = [[0 for j in range(m)] for i in range(len(height))]
#     for i,h in enumerate(height):
#         for j in range(h):
#             grid[i][j] = 1

#     return grid,m

class Solution:
    def trap(self, height: List[int]) -> int:
        """

        h = [1,3,1,2,3]
        #
        #  X  X
        #  X XX
        # XXXXX

        """

        tops = [height[0]]
        for h in height[1:]:
            if h > tops[-1]:
                tops.append(h)
            else: tops.append(tops[-1])

        max_right = height[-1]
        for i in range(len(height)-1,-1,-1):
            h = height[i]
            if max_right < h:
                max_right = h
            if tops[i] > max_right:
                tops[i] = max_right
        
        count = 0
        for i,h in enumerate(height):
            count += tops[i]-h

        return count

        # # grid,m = create_grid(height)
        # count = 0
        # for level in range(max(height)):
        #     temp = 0
        #     i = 0
        #     while i < len(height):
        #         # if grid[i][level]:
        #         if level < height[i]:
        #             i+=1
        #             while i < len(height) and level >= height[i]:
        #                 temp += 1
        #                 i += 1
        #             if i < len(height) and level < height[i]:
        #                 count += temp
        #                 temp = 0
        #         else:
        #             i += 1
        
        # return count

    # 4,2,0,3,2,5
    #      X
    # X    X
    # X  X X
    # XX XXX
    # XX XXX
