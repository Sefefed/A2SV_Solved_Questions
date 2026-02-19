class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        if n < 3:
            return 0
        for i in range(n-2):
            peri = nums[i] + nums[i+1] + nums[i+2]
            if nums[i] < nums[i+1] + nums[i+2]:
                return peri
        return 0        
        
