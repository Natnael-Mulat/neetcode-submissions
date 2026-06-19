class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row, n_col = len(matrix), len(matrix[0])
        l, r = 0, (n_row*n_col)-1
        while l<=r:
            m = (l+r)//2
            row, col = m//n_col, m%n_col
            if matrix[row][col] < target:
                l=m+1
            elif matrix[row][col] > target:
                r=m-1
            else:
                return True
        return False