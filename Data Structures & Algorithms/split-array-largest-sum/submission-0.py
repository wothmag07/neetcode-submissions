class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(maxSum):
            pieces = 1
            tot = 0
            for num in nums:
                if tot+num <= maxSum:
                    tot += num
                else:
                    if pieces > k:
                        return False
                    tot = num
                    pieces += 1
            return pieces <= k

        lptr, rptr = max(nums), sum(nums)
        while lptr < rptr:
            mid = (lptr + rptr) // 2
            if canSplit(mid):
                rptr = mid
            else:
                lptr = mid+1
        return lptr
        