class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def track(ind, path):
            if len(path) == k:
                res.append(path)
                return 
            if ind == n+1:
                return 
            track(ind+1, path+[ind])   
            track(ind+1, path)    
        track(1, [])
        return res
        
