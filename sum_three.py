from typing import List
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0:
            return [-1, 0, 1]
        result = []
        sum = 0
        i = num // 3 - 3
        j = i + 1
        k = j + 1
        while sum < num:
            i+= 1
            j+= 1
            k+= 1
            sum = i + j + k
            if sum == num:
                result.extend([i, j, k])
        return result        
            
            