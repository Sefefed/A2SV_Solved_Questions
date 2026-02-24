from collections import Counter
t = int(input())


for _ in range(t):
    result = []
    s = list(input())
    t = list(input())
    count_s = Counter(s)
    count_t = Counter(t)
    not_pos = False
    for ch in count_s:
        if ch not in count_t or count_s[ch] > count_t[ch]:
            not_pos = True
            break
    if not_pos:
        print("Impossible")  
        continue     
    i = 0 
    for ch in count_t:
        if ch in count_s:
            count_t[ch] -= count_s[ch]
    res = []            
    for ch, count in count_t.items():
        for i in range(count):
            res.append(ch)
    res.sort()
    i, j = 0, 0
    result = []
    while j < len(res) and i < len(s):
        if res[j] < s[i]:
            result.append(res[j])
            j += 1
        elif res[j] > s[i]:
            result.append(s[i])
            i += 1
        else:
            result.append(s[i])
            i += 1
    for c in range(i,len(s)):
        result.append(s[c])
    result.extend(res[j:])    
    print(''.join(result))           

              


    
    
    

                    
                
                
                    
    





        

