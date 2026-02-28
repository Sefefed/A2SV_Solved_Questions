t = int(input())

for _ in range(t):
  n, k = map(int, input().split())
  s = input()

  i, j = 0, k - 1
  cnt_b = s[i:j+1].count("B")
  ans = float('inf')
  while j < n:
    ans = min(ans, k - cnt_b)
    if s[i] == "B":
      cnt_b -= 1
    if j + 1 < n and s[j+1] == "B":
      cnt_b += 1
    i += 1
    j += 1
  print(ans)  
