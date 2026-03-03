n, k, q = map(int, input().split())
recipes = []
for _ in range(n):
  recipe = list(map(int, input().split()))
  recipes.append(recipe)
ques = []  
min_left = float('inf')
max_right = float('-inf')
for c in range(q):
  que = list(map(int, input().split()))
  if que[0] < min_left:
    min_left = que[0]
  if que[1] > max_right:
    max_right = que[1]  
  ques.append(que)
prefix_ans = [0] * (max_right - min_left + 1)
for left, right in recipes:
  if left > max_right or right < min_left:
    continue
  if left < min_left:
    prefix_ans[0] += 1
  else:
    prefix_ans[left - min_left] += 1
  if right < max_right:
    prefix_ans[right - min_left + 1] -= 1
for i in range(1, len(prefix_ans)):
  prefix_ans[i] += prefix_ans[i-1]
for i, num in enumerate(prefix_ans):
  if num >= k:
    prefix_ans[i] = 1
  else:
    prefix_ans[i] = 0
for i in range(1, len(prefix_ans)):
  prefix_ans[i] += prefix_ans[i-1]
for que_left, que_right in ques:
  print(prefix_ans[que_right - min_left] - prefix_ans[que_left - min_left - 1] if que_left - min_left - 1 > -1 else prefix_ans[que_right - min_left])
