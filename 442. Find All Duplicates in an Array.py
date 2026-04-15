class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        dup = []
        while i < n:
                correct = nums[i] - 1
                if nums[i] != nums[correct]:
                      nums[i], nums[correct] = nums[correct], nums[i]
                else:
                    i += 1
        for i in range(n):
            if nums[i] != i + 1:
                dup.append(nums[i])
        return dup        
