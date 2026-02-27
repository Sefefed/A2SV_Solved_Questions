from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        i1 = i2 = 0
        distinct1 = distinct2 = 0
        ans = 0

        for j in range(len(nums)):
            if freq1[nums[j]] == 0:
                distinct1 += 1
            freq1[nums[j]] += 1

            if freq2[nums[j]] == 0:
                distinct2 += 1
            freq2[nums[j]] += 1

            while distinct1 > k:
                freq1[nums[i1]] -= 1
                if freq1[nums[i1]] == 0:
                    distinct1 -= 1
                i1 += 1

            while distinct2 > k - 1:
                freq2[nums[i2]] -= 1
                if freq2[nums[i2]] == 0:
                    distinct2 -= 1
                i2 += 1

            ans += i2 - i1

        return ans
