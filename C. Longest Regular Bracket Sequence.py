s = input()
dic = {}
st = []
temp = []
for ch in s:
  if ch == "(":  
    st.append(ch)
    temp.append(ch)
  else:
    if not st and len(temp) > 0:
        dic[len(temp)] = dic.get(len(temp), 0) + 1
        temp.clear()
    elif st:
      st.pop()
      temp.append(ch)
n = len(temp)
tra_ = []
tra_cnt = 0
for i in range(n-1, -1, -1):
  if temp[i] == ")":
    tra_.append(temp[i])
  else:
    if tra_:
      tra_cnt += 2
      tra_.pop()
    else:
      if tra_cnt > 0:
        dic[tra_cnt] = dic.get(tra_cnt, 0) + 1
        tra_cnt = 0
if tra_cnt > 0:
  dic[tra_cnt] = dic.get(tra_cnt, 0) + 1      
if len(dic.keys()) > 0:      
  sorted_ = sorted(dic.keys())  
  print(sorted_[-1], dic[sorted_[-1]]) 
else:
  print(0, 1)     

