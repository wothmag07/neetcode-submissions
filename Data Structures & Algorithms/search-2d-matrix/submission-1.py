class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        lptr, rptr = 0, rows*cols - 1
        while lptr <= rptr:
            m = (lptr + rptr) // 2
            row, col = m // cols, m % cols
            if target > matrix[row][col]:
                lptr = m + 1
            elif target < matrix[row][col]:
                rptr = m - 1
            else:
                return True
        return False

        