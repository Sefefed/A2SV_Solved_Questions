n, m = map(int, input().split())

fir = list(map(int, input().split()))
sec = list(map(int, input().split()))

i, j = 0, 0
k, l = 0, 0
count = 0

while j < n and l < m:
  if fir[j] == sec[l]:
    while j < n - 1 and fir[j] == fir[j+1]:
      j += 1
    while l < m - 1 and sec[l] == sec[l + 1]:
      l += 1 
    count += (j - i + 1) * (l - k + 1) 
    j += 1
    l += 1
    i, k = j, l
  else:
    (i, j, k, l) = (i+1, j+1, k, l) if fir[j] < sec[l] else (i, j, k+1, l+1)
print(count)      




