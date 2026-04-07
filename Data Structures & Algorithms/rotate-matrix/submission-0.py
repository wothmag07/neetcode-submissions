class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        lptr, rptr = 0, len(matrix)-1
        while lptr < rptr:
            for i in range(rptr-lptr):
                tptr,bptr = lptr, rptr

                topleft = matrix[tptr][lptr+i]
                matrix[tptr][lptr+i] = matrix[bptr-i][lptr]

                matrix[bptr-i][lptr] = matrix[bptr][rptr-i]
                matrix[bptr][rptr-i] = matrix[tptr + i][rptr]
                matrix[tptr+i][rptr] = topleft
            
            rptr -= 1
            lptr += 1


        

        