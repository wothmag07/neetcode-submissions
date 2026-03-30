class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lptr, rptr = 0, 0

        while rptr < len(prices):
            if prices[lptr] < prices[rptr]:
                profit = prices[rptr] - prices[lptr]
                maxP = max(maxP, profit)
            else:
                lptr = rptr
            rptr += 1
        return maxP
                


        