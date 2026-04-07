class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for h in houses:
            l, r = 0, len(heaters) - 1
            cur_ = float('inf')
            while l <= r:
                mid = (l + r) // 2
                if heaters[mid] <=  h:
                    cur_ = min(cur_, abs(h - heaters[mid]))    
                    l = mid + 1                
                else:
                    cur_ = min(cur_, abs(h - heaters[mid]))
                    r = mid - 1
            ans = max(ans, cur_)        
        return ans        

       
        







        

        
