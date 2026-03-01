t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    prefix = []
    cnt0 = cnt1 = 0
    for i in range(n):
        if a[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
        prefix.append((cnt0, cnt1))

    flipped = False
    possible = True

    for i in range(n-1, -1, -1):
        cur = a[i]
        if flipped:
            cur = '1' if cur == '0' else '0'

        if cur != b[i]:
            zeros, ones = prefix[i]
            if zeros != ones:
                possible = False
                break
            flipped = not flipped

    print("YES" if possible else "NO")
