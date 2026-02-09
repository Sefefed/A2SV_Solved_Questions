from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)  
        
        # Step 2: use heap to get k most common
        return [num for num, count in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]