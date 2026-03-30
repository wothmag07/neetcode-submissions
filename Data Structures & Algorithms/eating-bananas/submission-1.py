class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            k = (low + high) // 2
            totaltime = 0
            for pile in piles:
                totaltime += math.ceil(pile/k)
            
            if totaltime <= h:
                res = k
                high = k - 1
            
            else:
                low = k + 1
        
        return res
        