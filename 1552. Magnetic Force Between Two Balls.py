class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        k = len(position)
        position.sort()
        ans = 0
        def isPos(m, ans, position):
            cnt = 1
            prev = position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= ans:
                    prev = position[i]
                    cnt += 1
                    if cnt >= m:
                        return True
            return False
        l, r =  1, position[-1] - position[0]
        while l <= r:
            mid = (l + r)// 2
            if isPos(m, mid, position):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1  
        return ans



                  
                
        
