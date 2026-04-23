class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(1, n):
            ans = max(ans, nums[i] - nums[i-1])
        return ans    
        
