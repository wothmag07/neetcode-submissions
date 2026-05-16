# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lptr, rptr = 1, n
        while lptr <= rptr:
            mid = (lptr + rptr) // 2
            res = guess(mid)
            if res < 0:
                rptr = mid-1
            elif res > 0:
                lptr = mid+1
            else:
                return mid


        