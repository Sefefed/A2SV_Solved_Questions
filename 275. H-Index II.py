class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(h):
            cnt = 0
            for i in range(len(citations)):
                if citations[i] >= h:
                    cnt += 1
            return cnt >= h        

        l, r = 0, len(citations)
        while l <= r:
            mid = (r + l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r     

