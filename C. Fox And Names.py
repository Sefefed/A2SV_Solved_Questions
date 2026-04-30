from collections import deque
n = int(input())
given = [input() for i in range(n)]
graph = [[] for i in range(26)]
for i in range(n-1):
  first = given[i]
  second = given[i+1]
  isFalse = True
  for j in range(min(len(first), len(second))):
    if first[j] != second[j]:
      u, v = ord(first[j]) - ord('a'), ord(second[j])-ord('a')
      graph[u].append(v)
      isFalse = False
      break
  if isFalse and len(first) > len(second):
    print('Impossible')
    exit() 
color = [0] * 26
ans = deque()   
def dfs(node):
  if color[node] == 1:
    return False
  if color[node] == 2:
    return True
  color[node] = 1
  for nei in graph[node]:
    if not dfs(nei):
      return False
  color[node] = 2
  ans.appendleft(chr(ord('a') + node))
  return True
for i in range(26):
  if color[i] == 0:
    if not dfs(i):
      print('Impossible')
      exit()  
print(''.join(list(ans)))       
