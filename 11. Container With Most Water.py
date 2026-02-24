class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_ = float('-inf')
        while i < j:
            area = (j - i) * min(height[i], height[j])
            if area > max_:
                max_ = area
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                if height[i+1] > height[j-1]:
                    j -= 1
                elif height[i+1] < height[j-1]:
                    i += 1
                else:
                    i += 1
                    j -= 1
        return max_                  

        
