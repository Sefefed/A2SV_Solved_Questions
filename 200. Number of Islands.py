class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        n, m = len(grid), len(grid[0])
        def dfs(row, col):
            if row < 0 or col < 0 or row >= n or col >= m or grid[row][col] == "0":
                return 
            grid[row][col] = "0"
            dfs(row, col-1)
            dfs(row-1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)  
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)    
        return count

