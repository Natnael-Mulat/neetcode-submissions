class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_rows, n_cols = len(matrix), len(matrix[0])
        l, r = 0, (m_rows * n_cols) - 1
        while l <= r:
            m = (l + r) // 2
            row, col = m // n_cols, m % n_cols
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True

        return False