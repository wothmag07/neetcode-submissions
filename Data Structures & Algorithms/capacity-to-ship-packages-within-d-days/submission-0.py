class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):
            tot = 0
            D = 1
            for weight in weights:
                if tot + weight > capacity:
                    D += 1
                    tot = 0
                tot += weight
            return D <= days
        
        lptr, rptr = max(weights), sum(weights)
        while lptr <= rptr:
            mid = (lptr + rptr) // 2
            if canShip(mid):
                rptr = mid-1
            else:
                lptr = mid+1
        return lptr

        