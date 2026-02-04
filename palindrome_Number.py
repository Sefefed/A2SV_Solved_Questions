class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        current = x
        ans = 0
        while current > 0:
            remainder = current % 10
            ans = ans * 10 + remainder
            current //= 10
            
        return ans == x
