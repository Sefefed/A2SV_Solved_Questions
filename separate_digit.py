from typing import List
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            num_str = str(num)
            for s in num_str:
                result.append(int(s))
        return result 