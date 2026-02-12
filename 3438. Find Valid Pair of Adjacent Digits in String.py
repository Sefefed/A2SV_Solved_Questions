class Solution:
    def findValidPair(self, s: str) -> str:
        digit_cnt = Counter(s)
        for i in range(1, len(s)):
            if int(s[i]) == digit_cnt[s[i]] and int(s[i-1]) == digit_cnt[s[i-1]] and s[i] != s[i - 1]:
                return s[i-1:i+1]
        return ""
