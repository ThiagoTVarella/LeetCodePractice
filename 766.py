def next_elem(matrix,i,j):
    if i+1 < len(matrix) and j+1 < len(matrix[0]):
        return matrix[i+1][j+1]
    else:
        return None

# next_elem = lambda matrix,i,j: matrix[i+1][j+1] if i<len(matrix)-1 and j<len(matrix)-1 else None 

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        min_mn = min(m,n)

        # Pre-full

        for j in range(n-1,0,-1):
            i = 0
            elem = matrix[i][j]
            while (next_el := next_elem(matrix,i,j)) is not None:
                if elem != next_el:
                    return False
                i,j = i+1,j+1

        # Full, min_mn 
        for i in range(m):
            j = 0
            elem = matrix[i][j]
            while (next_el := next_elem(matrix,i,j)) is not None:
                if elem != next_el:
                    return False
                i,j = i+1,j+1
        
        return True


# [36,86,7,94,71,59,10],
# [19,0,86,7,94,71,59]