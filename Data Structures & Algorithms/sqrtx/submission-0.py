class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lptr, rptr = 1, x // 2
        res = 0

        while lptr <= rptr:
            mid = (lptr + rptr) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                res = mid
                lptr = mid + 1
            else:
                rptr = mid - 1

        return res
        