class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict = {0:1}
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        ans = 0    
        for num in nums:
            if num % k in dict:
                ans += dict[num % k]  
            dict[num % k] = dict.get(num % k, 0) + 1
        return ans    
        
