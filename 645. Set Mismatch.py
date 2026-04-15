class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = (n * (n + 1)) // 2
        dup, lost = 0, 0
        for num in nums:
            if nums.count(num) > 1:
                dup = num
        lost = total_sum - (sum(nums) - dup)
        return [dup, lost]        



                
        
        
