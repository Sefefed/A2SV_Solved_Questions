n = int(input())

given_list = list(map(int, input().split()))

given_list.sort()

print(given_list[(n-1) // 2])
