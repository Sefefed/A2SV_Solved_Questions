class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ans = nums[0]
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum + num, num)
            max_ans = max(current_sum, max_ans)
        return max_ans    


        
        
