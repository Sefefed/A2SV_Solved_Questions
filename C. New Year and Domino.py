n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

right = [[0]*m for _ in range(n)]
down = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if j + 1 < m and board[i][j] == '.' and board[i][j+1] == '.':
            right[i][j] = 1
        if i + 1 < n and board[i][j] == '.' and board[i+1][j] == '.':
            down[i][j] = 1

acc_r = [[0]*(m+1) for _ in range(n+1)]
acc_d = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        acc_r[i][j] = right[i-1][j-1] + acc_r[i-1][j] + acc_r[i][j-1] - acc_r[i-1][j-1]
        acc_d[i][j] = down[i-1][j-1] + acc_d[i-1][j] + acc_d[i][j-1] - acc_d[i-1][j-1]

def area(p, x1, y1, x2, y2):
    return p[x2][y2] - p[x1-1][y2] - p[x2][y1-1] + p[x1-1][y1-1]

t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    res = 0
    if b < d:
        res += area(acc_r, a, b, c, d-1)
    if a < c:
        res += area(acc_d, a, b, c-1, d)
    print(res)
