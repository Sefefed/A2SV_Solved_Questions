class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        indegree = [0 for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        que = deque()
        for i in range(n):
            if indegree[i] == 0:
                que.append(i) 
        ance = [set() for i in range(n)]
        while que:
            node = que.popleft()
            for nei in graph[node]:
                ance[nei].add(node)
                for val in ance[node]:
                    if val not in ance[nei]:
                        ance[nei].add(val)
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    que.append(nei)    
        return [sorted(list(ance[i])) for i in range(n)]        






            
        




         
