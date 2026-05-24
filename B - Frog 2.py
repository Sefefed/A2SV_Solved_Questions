import sys
input = sys.stdin.readline
n, k = map(int, input().split())
wgt = list(map(int, input().split()))
dp = [float('inf')] * n
dp[0] = 0
for i in range(1, n):
    for j in range(1, k + 1):
        if i - j < 0:
            break
        dp[i] = min(dp[i], dp[i-j] + abs(wgt[i] - wgt[i-j]))
print(dp[n-1])
