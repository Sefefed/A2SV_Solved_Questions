class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, num in enumerate(citations):
            if num >= i + 1:
                h = i + 1
        return h        


        
