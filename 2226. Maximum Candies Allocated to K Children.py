class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sum_ = sum(candies)
        if sum_ < k:
            return 0

        def check(mid):
            cnt = 0
            for num in candies:
                cnt += num // mid
            return cnt >= k    
        ans = 0    
        l, r = 1, max(candies)
        while l <= r:
            mid = (l + r)// 2
            if not check(mid):
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        return ans    






        
