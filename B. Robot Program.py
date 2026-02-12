t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + (1 if s[i] == 'R' else -1)

    first_hit = -1
    for i in range(1, n + 1):
        if x + pref[i] == 0:
            first_hit = i
            break

    if first_hit == -1 or first_hit > k:
        print(0)
        continue

    answer = 1
    remaining = k - first_hit

    cycle_len = -1
    for i in range(1, n + 1):
        if pref[i] == 0:
            cycle_len = i
            break

    if cycle_len != -1:
        answer += remaining // cycle_len

    print(answer)
