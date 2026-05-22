class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dp(i):
            if i >= n:
                return 0
            if i not in memo:
                memo[i] = max(nums[i] + dp(i + 2), nums[i] + dp(i + 3)) 
            return memo[i]
        return max(dp(0), dp(1))


        
