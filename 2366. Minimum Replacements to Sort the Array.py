class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        comp = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > comp:
                if nums[i] < 2 * comp:
                    ops += 1
                    comp = nums[i] // 2
                else:  
                    if nums[i] % comp != 0:
                        ops += (nums[i] // comp)
                        comp = nums[i] // (nums[i] // comp + 1)
                    else:
                        ops += (nums[i] // comp) - 1
            else:
                comp = nums[i]
        return ops



        
