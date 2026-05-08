class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if len(heap) < k:
                    heappush(heap, -matrix[i][j])
                elif matrix[i][j] < -heap[0]:
                    heapreplace(heap, -matrix[i][j])  
        return -heap[0]              

        

        
