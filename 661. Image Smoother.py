class Solution:
    
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        def in_bound(row, col):
          return 0 <= row < m and 0 <= col < n
        direction = [(-1, 0), (-1, 1), (1, 0), (1, 1), (0, 1), (1, -1),(0, -1), (-1, -1)]
        mat = [[0]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                sum_ = img[row][col]
                cnt = 1
                for d1, d2 in direction:
                    if in_bound(row+d1, col+d2):
                        sum_ += img[row + d1][col + d2]
                        cnt += 1
                mat[row][col] = sum_//cnt
                
        return mat
       
