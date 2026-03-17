class Solution:
    def myPow(self, x: float, n: int) -> float:        
        isPos = True if n >= 0 else False
        n = abs(n)      
        def res(x, n):
            if n % 2 == 0:
                is_Odd = False
            else:
                is_Odd = True 
            if n == 0:
                return 1    
            if n == 1:
                return x
            if not is_Odd:
                return res(x*x, (n//2))
            else:
                return x * res(x*x, (n-1)//2)

        return res(x, n) if isPos else 1 / res(x, n) 
        
