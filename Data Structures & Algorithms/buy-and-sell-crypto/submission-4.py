class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = prices[0]
        maxprofit = float("-inf")
        for price in prices:
            maxprofit = max(maxprofit, price-buy)
            buy = min(buy, price)
        return maxprofit
        