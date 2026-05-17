class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        lptr, rptr = 0, (m*n) -1

        while lptr <= rptr:
            mid = (lptr + rptr) // 2
            r, c = mid//n, mid%n
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                lptr = mid + 1
            else:
                rptr = mid - 1
        return False