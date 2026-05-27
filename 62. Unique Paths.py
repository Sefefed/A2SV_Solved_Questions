class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) not in memo:
                if i + 1 < m and j + 1 < n:
                    memo[(i, j)] = dp(i + 1, j) + dp(i, j + 1) 
                elif i + 1 < m:
                    memo[(i, j)] = dp(i + 1, j)
                elif j + 1 < n:
                    memo[(i, j)] = dp(i, j + 1)         
            return memo[(i, j)]
        return dp(0, 0)    
