class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        dict = {}
        for i in range(n - 1, -1, -1):
            if s[i] not in dict:
                dict[s[i]] = i
        i, j = 0, dict[s[i]]   
        res = []     
        while j < n and i < n:
            start = i
            while i < j:
                i += 1
                if dict[s[i]] > j:
                    j = dict[s[i]]
            res.append(j - start + 1)
            if j < n - 1:
              j = dict[s[j+1]]   
            i += 1   
        return res     
            
