n, m = map(int, input().split())
sp = []
parent = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]
def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]  
def union(x, y):
  root1 = find(x)
  root2 = find(y)
  if root1 == root2:
    return
  if size[root1] < size[root2]:
    root1, root2 = root2, root1
  parent[root2] = root1
  size[root1] += size[root2]   
for _ in range(m):
  bi, ci, wi = map(int, input().split())
  sp.append((bi,ci, wi))
sp.sort(key=lambda x:x[2]) 
ans = 0
for bi,ci, wi in sp:
  if find(bi) != find(ci):
    union(bi,ci)
    ans += wi
print(ans)

 

