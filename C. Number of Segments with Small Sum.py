n, s = map(int, input().split())
arr = list(map(int, input().split()))
sum_ = 0
count = 0
 
i = 0
 
for j in range(n):
  sum_ += arr[j]
  while sum_ > s:
    sum_ -= arr[i]
    i += 1
  count += j - i + 1
print(count)   
