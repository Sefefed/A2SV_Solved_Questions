class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = {0:1}
        count = 0
        for i in range(len(nums)):
            if i > 0:
             nums[i] += nums[i-1]
            if nums[i] - goal in prefix_count:
                count += prefix_count[nums[i] - goal]
            prefix_count[nums[i]] = prefix_count.get(nums[i], 0) + 1
        return count        
        
