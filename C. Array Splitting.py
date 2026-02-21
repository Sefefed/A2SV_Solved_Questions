n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(a[-1] - a[0])
elif k == n:
    print(0)
else:
    diff = [a[i+1] - a[i] for i in range(n-1)]
    diff.sort(reverse=True)
    print(a[-1] - a[0] - sum(diff[:k-1]))
