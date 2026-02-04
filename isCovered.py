from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right+1):
            covered = False
            for i, interval in enumerate(ranges):
                if interval[0] <= num <= interval[1]:
                    covered = True
                    break
            if not covered:
                return False
        return True


        