class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        visited = [False for i in range(n)]
        def dfs(node, cur):
                if node == n-1:
                    ans.append(cur[:])
                    return
                for num in graph[node]:
                    cur.append(num)
                    dfs(num, cur)
                    cur.pop()

        dfs(0, [0])           
        return ans
        
