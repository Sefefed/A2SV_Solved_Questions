class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pre_sum = [0] * n
        for a, b, c in shifts:
            if c == 0:
                pre_sum[a] += -1
                if b+1 < n:
                   pre_sum[b+1] += 1
            else:
                pre_sum[a] += 1
                if b+1 < n:
                    pre_sum[b+1] -= 1 
        for i in range(1, n):
            pre_sum[i] += pre_sum[i-1]            
        tar = list(s)       
        for i, ch in enumerate(tar):
            val = 97 + (ord(ch) + pre_sum[i] - 97) % 26
            tar[i] = chr(val)
        return "".join(tar)    

