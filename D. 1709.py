t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  k = 0
  ops = []
  for i in range(n):
    for j in range(0, n - i - 1):
      if a[j] > a[j+1]:
        k += 1
        ops.append([1, j+1])
        a[j], a[j+1] = a[j+1], a[j]
      if b[j] > b[j+1]:
        k += 1
        ops.append([2, j+1])
        b[j], b[j+1] = b[j+1], b[j] 
  for c in range(n):
    if a[c] > b[c]:
      k += 1
      ops.append([3, c + 1]) 
  print(k)      
  for op in ops:
    print(*op)  

      
