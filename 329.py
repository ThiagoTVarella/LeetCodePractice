class Solution:

    def recursive(self,i,j):

        if 0 <= i < self.n and 0 <= j < self.m: 

            if self.memo[i][j] != 0:
                return self.memo[i][j]

            # return the max path for each direction
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            aux_max = 1
            for dx,dy in dirs:
                if 0 <= i+dx < self.n and 0 <= j+dy < self.m: 
                    if self.matrix[i+dx][j+dy] > self.matrix[i][j]:
                        aux_max = max(self.recursive(i+dx,j+dy)+1,aux_max)

            self.memo[i][j] = aux_max 
            return aux_max
        
        else:
            return -1

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.n = len(matrix) # 2
        self.m = len(matrix[0]) # 2

        self.memo = [[0]*self.m for _ in range(self.n)] #[0,0][0,0]
        longest = 0

        for i in range(self.n):
            for j in range(self.m):
                self.recursive(i,j)
                longest = max(longest,self.memo[i][j])

        return longest        

# 1 5
# 2 3

# Explicit that this is my brute force
# Memorize hard problems