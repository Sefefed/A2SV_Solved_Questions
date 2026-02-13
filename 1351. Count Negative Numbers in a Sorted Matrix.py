class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count_neg = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] < 0:
                    count_neg += 1
        return count_neg            
