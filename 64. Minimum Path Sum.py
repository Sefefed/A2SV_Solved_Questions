class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        n, m = len(grid), len(grid[0])
        def dp(i, j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            if (i, j) not in memo:
                if i + 1 < n and j + 1 < m:
                    memo[(i, j)] = grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))
                elif i + 1 < n:
                    memo[(i, j)] = grid[i][j] + dp(i + 1, j)    
                else:
                    memo[(i, j)] = grid[i][j] + dp(i, j + 1) 
            return memo[(i, j)]    
        return dp(0, 0)           

