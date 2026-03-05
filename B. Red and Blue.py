t = int(input())

for _ in range(t):
  n = int(input())
  arr_r = list(map(int, input().split()))
  m = int(input())
  arr_b = list(map(int, input().split()))

  for i in range(1, n):
    arr_r[i] += arr_r[i-1]
  max_r = max(arr_r)  
  for j in range(1, m):
    arr_b[j] += arr_b[j-1]
  max_b = max(arr_b)  
  print(max(0, max_b, max_r, max_b + max_r))
