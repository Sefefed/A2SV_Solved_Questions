class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_n = len(matrix)
        col_n = len(matrix[0])
        row_zero = set()
        col_zero = set()
        for i in range(row_n):
            for j in range(col_n):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        
        for r in row_zero:
            matrix[r] = [0] * col_n
        for k in range(row_n):
            for c in col_zero:
                matrix[k][c] = 0
        return matrix        

           

