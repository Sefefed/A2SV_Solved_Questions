from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

i, j = 0, 0
max_ = 0
cnt = defaultdict(int)
for j in range(n):
  cnt[arr[j]] += 1
  if len(cnt.keys()) > k:
    cnt[arr[i]] -= 1
    if cnt[arr[i]] == 0:
      del cnt[arr[i]]
    i += 1
  if j - i + 1 > max_:
    max_ = j - i + 1
    l, r = i + 1, j + 1
print(l, r)    


