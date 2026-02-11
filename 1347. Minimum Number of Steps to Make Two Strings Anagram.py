from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        n = len(s)
        steps = 0
        count_t = Counter(t)
        count_s = Counter(s)
        for ch in t:
            if ch in count_s:
                count_s[ch] -= 1
                count_t[ch] -= 1
                if count_s[ch] == 0:
                    del count_s[ch]
        for ch in count_t:
            steps += count_t[ch]

        return steps


        
