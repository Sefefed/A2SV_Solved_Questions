t = int(input())

for _ in range(t):
  n = int(input())
  given_str = input()

  if "aa" in given_str:
    print(2)
    continue
  min_len = n + 1
  index_a = []
  for i, char in enumerate(given_str):
    if char == "a":
      index_a.append(i)
  for indices in index_a:
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0
    for ch in given_str[indices:indices + 7]:
      if ch == "a":
        cnt_a += 1
        if cnt_a > cnt_b and cnt_a > cnt_c and cnt_a + cnt_b + cnt_c > 2:
           min_len = min(min_len, cnt_a + cnt_b + cnt_c)  
      elif ch == "b":
        cnt_b += 1
      else:
        cnt_c += 1 
    if cnt_a > cnt_b and cnt_a > cnt_c and cnt_a + cnt_b + cnt_c > 2:
      min_len = min(min_len, cnt_a + cnt_b + cnt_c)
  if min_len == len(given_str) + 1:
    print(-1)
  else:
    print(min_len)  
