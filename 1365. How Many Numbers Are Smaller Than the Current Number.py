class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            count = 0
            for j, num in enumerate(nums):
                if j != i and nums[j] < nums[i]:
                    count += 1
            result.append(count)        
        return result    
