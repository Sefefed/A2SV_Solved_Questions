class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def track(ind, path):
            if ind == n:
                res.append(path)
                return 
            track(ind+1, path)
            track(ind+1, path+[nums[ind]]) 
        track(0, [])
        return res    
            

        
