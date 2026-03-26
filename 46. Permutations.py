class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def calcPer(built, remaining):
            if not remaining:
                res.append(built)
                return 
            for i in range(len(remaining)):
                calcPer(built+[remaining[i]], remaining[:i] + remaining[i+1:])  

        calcPer([], nums)  
        return res       







            
    
        
