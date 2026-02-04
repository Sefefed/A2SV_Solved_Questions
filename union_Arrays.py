class Solution:    
    def findUnion(self, a, b):
       a.extend(b)
       a = list(set(a))      
       return a    