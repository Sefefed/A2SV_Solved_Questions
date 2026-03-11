from collections import deque
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        que = deque(nums)
        ops = 0
        while que:
            if que[0] == 1:
                que.popleft()
            elif len(que) < 3 and que[0] == 0:
                break
            else:
                que[1] = 1 - que[1]
                que[2] = 1 - que[2]   
                que.popleft() 
                ops += 1
        return ops if not que else -1        


            
        
