class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_s = Counter(s)
        count_ord = Counter(order)
        res = []
        for ch in order:
            if ch in count_s:
                for i in range(count_s[ch]):
                    res.append(ch)
                del count_s[ch] 
        for cha in count_s:
            for i in range(count_s[cha]):
                res.append(cha)   
        return ''.join(res)         


