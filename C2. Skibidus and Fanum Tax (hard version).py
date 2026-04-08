t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  b.sort()
  def bs(ind, prev):
    l, r = 0, len(b) - 1
    ans = a[ind]
    while l <= r:
      mid = (l + r) // 2
      if b[mid] - a[ind] >= prev:
        ans = b[mid] - a[ind]
        r = mid - 1
      else:
        l = mid + 1
    if a[ind] < ans and a[ind] >= prev:
      pass
    else:
      a[ind] = ans
  a[0] = min(a[0], b[0] - a[0])
  for j in range(1, len(a)):
    bs(j, a[j-1])
  print("YES" if a == sorted(a) else "NO")

