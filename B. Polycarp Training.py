cont = int(input())
contests = list(map(int, input().split()))

contests.sort()
days = 0
i = 0 # index to track the contests
while i < cont:
  if contests[i] > days:
    days += 1
  i += 1  

print(days)  
