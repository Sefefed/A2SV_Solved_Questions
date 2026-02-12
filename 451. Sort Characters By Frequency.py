class Solution:
    def frequencySort(self, s: str) -> str:
        count_rep = Counter(s)
        sorted_s = sorted(count_rep, key=lambda key:count_rep[key], reverse=True)
        res = []
        for ch in sorted_s:
            n = count_rep[ch]
            for i in range(n):
                res.append(ch)
        return "".join(res)

        
