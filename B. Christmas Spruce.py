import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for i in range(2,n+1):
      p = int(input())
      tree[p-1].append(i)

    for child in tree:
      if not child:
        continue

      c = 0
      for e in child:
        if not tree[e-1]:
          c += 1
      if c < 3:
        print("No")
        exit()
    print("Yes")
solve()

