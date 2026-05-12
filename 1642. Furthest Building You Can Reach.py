from heapq import heapify, heappush, heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # at one time it either enters the heap or brick is used
        heap = []
        ans = 0
        for i in range(len(heights)):
            if i == 0:
                if len(heap) < ladders:
                    heappush(heap, 0)
            else:
                if len(heap) < ladders:
                    heappush(heap, max(0, heights[i] - heights[i - 1]))
                elif ladders > 0 and heap[0] <= bricks and max(0, heights[i] - heights[i-1]) > heap[0]:
                     bricks -= heappop(heap)
                     heappush(heap, max(0, heights[i] - heights[i-1]))
                elif heights[i] - heights[i-1] <= bricks:
                    bricks -= max(0, heights[i] - heights[i - 1])
                else:
                    return i - 1
        else:
            return i            










        
        
