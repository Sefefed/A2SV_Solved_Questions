class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        pos_row = -1
        l, r = 0, m-1
        while l <= r:
            mid = (l + r)// 2
            if matrix[mid][n-1] >= target:
                pos_row = mid
                r = mid - 1
            else:
                l = mid + 1    
        if pos_row == -1:
            return False
        i, j = 0, n - 1
        while i <= j:
            midd = (i+j) // 2
            if matrix[pos_row][midd] == target:
                return True
            elif matrix[pos_row][midd] > target:   
                j = midd - 1
            else:
                i = midd + 1
        return False














        
