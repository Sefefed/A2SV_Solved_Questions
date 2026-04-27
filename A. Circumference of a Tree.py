from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
adj = [[] for i in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
def bfs(node):
    dis = [-1] * (n + 1)
    dis[node] = 0
    tar_ = node
    max_dis = 0
    queue = deque([node])
    while queue:
        node = queue.popleft()
        for nei in adj[node]:
            if dis[nei] == -1:
                dis[nei] = dis[node] + 1
                queue.append(nei)
                if dis[nei] > max_dis:
                    max_dis = dis[nei]
                    tar_ = nei
    return max_dis, tar_
d, tar_ = bfs(1)
answer, tarr = bfs(tar_)
print(3 * answer)
