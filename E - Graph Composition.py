for _ in range(int(input())):
  n, m1, m2 = map(int, input().split())
  sizef = [1 for i in range(n + 1)]
  sizeg = [1 for i in range(n + 1)]
  pf = [i for i in range(n + 1)]
  pg = [i for i in range(n + 1)]
  cf = cg = n
  ans = 0
  def find(x, parent):
    if x != parent[x]:
      parent[x] = find(parent[x], parent)
    return parent[x]
  def union(x, y, parent, size):
    root1 = find(x, parent)
    root2 = find(y, parent)
    if root1 == root2:
      return True
    if size[root1] < size[root2]:
      root1, root2 = root2, root1
    parent[root2] = root1
    size[root1] += size[root2]
    return False  
  set_ = set()    
  for _ in range(m1):
    u, v = map(int, input().split())
    set_.add((u, v))
  for _ in range(m2):
    u, v = map(int, input().split())
    check = union(u, v, pg, sizeg)
    if not check:
      cg -= 1
  for u, v in set_:
    if find(u, pg) == find(v, pg):
      if not union(u, v, pf, sizef):
        cf -= 1
    else:
      ans += 1
  print(ans + abs(cf - cg))        


