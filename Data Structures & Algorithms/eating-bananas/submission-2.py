class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatAllBananas(speed):
            hours = 0
            for pile in piles:
                hours += (pile-1) // speed+1
            return hours <= h

        lptr, rptr = 1, max(piles)
        while lptr <= rptr:
            mid = (lptr + rptr) // 2
            if canEatAllBananas(mid):
                rptr = mid-1
            else:
                lptr = mid+1
        return lptr