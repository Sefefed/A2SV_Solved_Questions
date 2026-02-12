class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_n = len(matrix)
        col_n = len(matrix[0])
        T_matrix = [[0] * row_n for i in range(col_n)]
        
        for i in range(col_n):
            for j in range(row_n):
                T_matrix[i][j] = matrix[j][i]
        return T_matrix        
