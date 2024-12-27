def dfs(area,grid,islandID,i,j):

    if grid[i][j] == 1:

        grid[i][j] = islandID
        area += 1

        n = len(grid)
        m = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for dx,dy in directions:
            if 0 <= i+dx < n and 0 <= j+dy < m:
                if grid[i+dx][j+dy] == 1:
                    area,grid = dfs(area,grid,islandID,i+dx,j+dy)
    
    return area,grid


def largestIsland(grid) -> int:

    n = len(grid)
    m = len(grid[0])
    islandID = 2
    areas = {}

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                area,grid = dfs(0,grid,islandID,i,j)
                areas[islandID] = area 
                islandID += 1 
            

    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    max_area = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                
                areas_aux = [0,0,0,0]
                for dir in range(len(directions)):
                    dx,dy = directions[dir]
                    if 0 <= i+dx < n and 0 <= j+dy < m and grid[i+dx][j+dy] in areas:
                        areas_aux[dir] = areas[grid[i+dx][j+dy]]
                
                areas_aux.sort()
                max_area_temp = areas_aux[2]+areas_aux[3]+1
                max_area = max(max_area,max_area_temp)                    
    
    return max_area 

# 1 1 0
# 0 0 1
# 0 0 1
# 1 1 0

grid = [[1,1,0],[0,0,1],[0,0,1],[1,1,0]]
grid = largestIsland(grid)
print(grid)