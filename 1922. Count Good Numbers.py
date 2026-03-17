import math
class Solution:
    def countGoodNumbers(self, m: int) -> int:
        MOD = pow(10, 9) + 7  
        odd_dig = even_dig = m//2
        if m % 2 != 0:
            even_dig += 1
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
                return ((res(x, (n//2)) % MOD) ** 2) % MOD
            else:
                return (x * (((res(x, (n-1)//2) % MOD) ** 2) % MOD)) % MOD
            
        return (res(5, even_dig) * res(4, odd_dig)) % MOD    

        

        
