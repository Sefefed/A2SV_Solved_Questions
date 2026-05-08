from heapq import heappop, heappush, heappushpop, heapreplace
n = int(input())
heap = []
ans = []
def getMin():
  return heap[0]
def insert(x):
  heappush(heap, x)
def removeMin():
  heappop(heap)
for _ in range(n):
   ins = input().split()
   if ins[0] == "insert":
     insert(int(ins[1]))
     ans.append(f"insert {ins[1]}")
   elif ins[0] == "removeMin":
     if not heap:
        heappush(heap, 1)
        ans.append("insert 1")
     heappop(heap)
     ans.append("removeMin")
   elif ins[0] == "getMin":
     while heap and getMin() < int(ins[1]):
       removeMin()
       ans.append("removeMin")
     if not heap or getMin() != int(ins[1]):  
        insert(int(ins[1]))
        ans.append(f"insert {ins[1]}") 
     ans.append(f"getMin {ins[1]}")
print(len(ans))  
for each in ans:
  print(each)   


