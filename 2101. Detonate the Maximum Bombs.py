from collections import deque
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 0
        def bfs(start, idx):
            que = deque([start])
            visited = set()
            visited.add(idx)
            cnt = 1
            while que:
                cx, cy, cz = que.popleft()
                for i, bomb in enumerate(bombs):
                    if i not in visited:
                        dis = math.pow(bomb[0]-cx, 2) + math.pow(bomb[1]-cy, 2)
                        if dis <= math.pow(cz, 2):
                            cnt += 1
                            que.append(bomb)
                            visited.add(i)
            return cnt
        for i, bomb in enumerate(bombs):
            ans = max(ans, bfs(bomb, i))        
        return ans                





