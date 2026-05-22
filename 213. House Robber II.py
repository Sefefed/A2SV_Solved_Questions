class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = {}
        def dp(i, flag):
            if i >= n:
                return 0
            if i == n - 1 and flag == 0:
                return 0    
            if (i, flag) not in memo:
                memo[(i, flag)] = max(nums[i] + dp(i + 2, flag), dp(i + 1, flag)) 
            return memo[(i, flag)]
        return max(dp(0, 0), dp(1, 1))


        
