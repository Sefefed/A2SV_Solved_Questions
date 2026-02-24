t = int(input())

for _ in range(t):
  s = input().strip()
  n = len(s)
  i = 0
  res = []
  i, j = 0, 0
  while j < n:
    if j == n - 1 and s[i] == s[j]:
      if j - i == 0 and s[i] not in res:
        res.append(s[i])
      if (j - i) % 2 == 0 and s[i] not in res:
        res.append(s[i])  
    if s[i] == s[j]:
      j += 1
    else:
      if (j - i) % 2 == 1 and s[i] not in res:
        res.append(s[i])
      i = j  
  res.sort()
  print(''.join(res))    


