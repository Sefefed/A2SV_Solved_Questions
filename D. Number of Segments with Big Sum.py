n, s = map(int, input().split())
arr = list(map(int, input().split()))
sum_ = 0
count = 0
 
i = 0
 
for j in range(n):
  sum_ += arr[j]
  if sum_ >= s:
    count += 1
  count += i 
  while i < n and sum_ - arr[i] >= s:
    sum_ -= arr[i]
    count += 1
    i += 1 
print(count)    
