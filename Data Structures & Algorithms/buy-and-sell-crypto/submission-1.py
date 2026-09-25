class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        l, r, maxProfit = 0, 1, 0
        while r < len(prices):
            if prices[r] > prices[l]: # price raised
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return maxProfit

