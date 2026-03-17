class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        mid = float('-inf')
        st = []
        for i in range(n-1, -1, -1):
            if nums[i] < mid:
                return True
            while st and nums[i] > st[-1]:
                mid = st.pop()
            st.append(nums[i])  
        return False          
        
