class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        n, m = len(heights), len(heights[0])    
        pac = [[False for i in range(m)] for j in range(n)]
        atl = [[False for i in range(m)] for j in range(n)]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < m and 
                    not visited[nr][nc] and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
        for i in range(n):
            dfs(i, 0, pac)
        for j in range(m):
            dfs(0, j, pac)
        for i in range(n):
            dfs(i, m - 1, atl)
        for j in range(m):
            dfs(n - 1, j, atl)
        res = []
        for i in range(n):
            for j in range(m):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        return res
