class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we need to find a sequence of growing numbers
        # 10, 2, 5, 6, 7, 1 - we need to position l to 1, r to 4 => this will return profit
        # once prices[r] < prices[l], we need to start count from minimal number => l = r, r += 1

        l, r, maxProfit = 0, 1, 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit

        