class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(i, built, arr):
            if i == n:
                if built == sorted(built) and len(built) > 1 and built not in res:
                    res.append(built)
                return    
            backtrack(i+1, built + [arr[i]], arr)
            backtrack(i+1, built, arr)  
        backtrack(0, [], nums)    
        return res 
