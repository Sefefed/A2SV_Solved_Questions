t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  if n < 3:
   print(len(arr))
   print(*arr)
   continue
  inc = True if arr[1] > arr[0] else False     
  i, j = 0, 1
  res = []
  res.append(arr[0])
  
  while j < n:
    if arr[j] > arr[j-1] and inc:
       j += 1
    elif arr[j] < arr[j-1] and not inc:
      j += 1
    else:
         res.append(arr[j-1])
         i = j - 1
         inc = not inc
         j += 1
  res.append(arr[-1])       
      
  print(len(res))
  print(*res)
