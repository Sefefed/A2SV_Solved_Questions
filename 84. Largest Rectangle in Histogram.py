from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        for i, height in enumerate(heights):
            while st and heights[st[-1]] >=height:
                right[st[-1]] = i
                st.pop()
            if st:
                left[i] = st[-1]    
            st.append(i)
        return max(heig * (right[i] - left[i] - 1) for i, heig in enumerate(heights))    


        
