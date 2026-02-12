from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        changed.sort()
        count_num =  Counter(changed)
        ans = []
        for x in changed:
            if count_num[x] == 0:
                continue
            count_num[x] -= 1
            if count_num[x * 2] <= 0:
                return []    
            count_num[x * 2] -= 1
            ans.append(x)   
        return ans 
