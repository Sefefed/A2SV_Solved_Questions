class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        num_arr, last = 0, float('-inf')
        for left, right in sorted(points, key=lambda x:x[1]):
            if left > last:
                num_arr += 1
                last = right
        return num_arr        


        
