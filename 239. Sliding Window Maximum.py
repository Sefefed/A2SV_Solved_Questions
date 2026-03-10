from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deq = deque()
        result = []
        for i, num in enumerate(nums):
            if deq and deq[0] <= i-k:
                deq.popleft()
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)
            if i >= k-1:
                result.append(nums[deq[0]])
        return result


        
