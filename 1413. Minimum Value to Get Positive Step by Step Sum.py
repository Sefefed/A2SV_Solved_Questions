class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        min_pre = min(nums)    
        return 1 - min_pre if min_pre <= 0 else 1

        
