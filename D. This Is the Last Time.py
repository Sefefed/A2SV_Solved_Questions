t = int(input())

for _ in range(t):
  n, k = map(int, input().split())
  arr = []
  for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
  arr.sort(key=lambda x:x[0])
  for a, b, c in arr:
    if a <= k <= b and c >= k:
      k = c
  print(k)    
