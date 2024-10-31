class Solution:

    def floodfilldfs(self,grid: List[List[str]], i: int, j: int) -> List[List[str]]:
        dirx = [0,0,1,-1]
        diry = [1,-1,0,0]
        for direc in range(4):
            new_i = i+dirx[direc]
            new_j = j+diry[direc]
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                if grid[new_i][new_j] == "1":
                    grid[new_i][new_j] = "0"
                    grid = self.floodfill(grid,new_i,new_j)
        return grid

    def floodfillbfs(self,grid: List[List[str]], i: int, j: int) -> List[List[str]]:

        queue = [(i,j)]
        grid[i][j] = '0'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            x,y = queue.pop(0)
            
            for dx,dy in directions:
                nx = x+dx
                ny = y+dy

                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        queue.append((nx,ny))

        return grid

    def numIslands(self, grid: List[List[str]]) -> int:
        # Go through each element of the grid
        # If land, increase count and flood that island
        # Return count

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    grid = self.floodfillbfs(grid,i,j)
        
        return count

