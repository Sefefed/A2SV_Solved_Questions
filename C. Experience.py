n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
exp = [0 for i in range(n + 1)]
size = [1 for i in range(n + 1)]
def find(x):
  if x != parent[x]:
    return find(parent[x])
  return x
def union(x, y):
  root1 = find(x)
  root2 = find(y)
  if root1 == root2:
    return 
  if size[root1] < size[root2]:
    root1, root2 = root2, root1
  parent[root2] = root1  
  exp[root2] -= exp[root1]
  size[root1] += size[root2]
inc = set()  
for _ in range(m):
  query = input().split()
  if query[0] == "join":
    x, y = int(query[1]), int(query[2])
    union(x, y)
  elif query[0] == "add":
    root = find(int(query[1]))
    exp[root] += int(query[2])
  else:
    x = int(query[1])
    ans = exp[x]
    while x != parent[x]:
      ans += exp[parent[x]]
      x = parent[x]
    print(ans)
