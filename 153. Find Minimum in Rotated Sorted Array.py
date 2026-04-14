class Solution:
    def findMin(self, nums: List[int]) -> int:
        def minn(l, r):
            if l == r:
                return nums[l]
            mid = (l + r) // 2    
            left_min = minn(l, mid)
            right_min = minn(mid + 1, r) 
            return min(left_min, right_min)  
        return minn(0, len(nums)-1)     
        
