class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])

        lptr, rptr = 0, cols-1
        tptr, bptr = 0, rows-1

        res = []

        while tptr <= bptr and lptr <= rptr:

            for i in range(lptr, rptr+1):
                res.append(matrix[tptr][i])
            tptr += 1
            for i in range(tptr, bptr+1):
                res.append(matrix[i][rptr])
            rptr -= 1
            if tptr <= bptr:
                for i in range(rptr, lptr-1, -1):
                    res.append(matrix[bptr][i])
                bptr -= 1
            
            if lptr <= rptr:
                for i in range(bptr, tptr-1, -1):
                    res.append(matrix[i][lptr])
                lptr += 1
            
        return res
        
        