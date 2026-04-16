t = int(input())
for _ in range(t):
  m = int(input())
  arr = list(map(int, input().split()))
  ops = 0
  def merge(left, right):
    global ops
    if left[-1] < right[0]:
      return left + right
    else:
      ops += 1
      return right + left
  def mergeSort(l, r, arr):
    if l == r:
      return [arr[l]]
    mid = (l + r) // 2
    left = mergeSort(l, mid, arr)  
    right = mergeSort(mid + 1, r, arr)
    return merge(left, right)
  if sorted(arr) != mergeSort(0, m-1, arr):
    print(-1)
  else:
    print(ops)  
   
    
    
