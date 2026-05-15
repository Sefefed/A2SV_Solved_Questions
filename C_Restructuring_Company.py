n, q = map(int, input().split())
parent = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]
nxt_ups = [i + 1 for i in range(n + 1)]
def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]  
def union(a, b):
  root1 = find(a)
  root2 = find(b)
  if root1 == root2:
    return
  if size[root1] < size[root2]:
    root1, root2 = root2, root1
  parent[root2] = root1
  size[root1] += size[root2]  
for _ in range(q):
  t, x, y = map(int, input().split())  
  if t == 1:
    union(x, y)
  elif t == 2:
    i = nxt_ups[x]
    while i <= y:
      union(x, i)
      nxt = nxt_ups[i]
      nxt_ups[i] = y + 1
      i = nxt
  else:
    print("YES" if find(x) == find(y) else "NO")
