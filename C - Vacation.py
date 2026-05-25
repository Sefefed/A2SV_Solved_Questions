n = int(input())
dp = [[0, 0, 0] for i in range(n)]
a, b, c = map(int, input().split())
dp[0][0] = a
dp[0][1] = b
dp[0][2] = c
for i in range(1, n):
  a, b, c = map(int, input().split())
  dp[i][0] = a + max(dp[i-1][1], dp[i-1][2])
  dp[i][1] = b + max(dp[i-1][0], dp[i-1][2])
  dp[i][2] = c + max(dp[i-1][0], dp[i-1][1])
print(max(dp[n-1]))  
  
