class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, maxP = 0, 1, 0

        while i < len(prices) and j < len(prices):
            if prices[i] >= prices[j]:
                i = j
                j = i + 1
            else:
                maxP = max(maxP, prices[j] - prices[i])
                j += 1
        return maxP
        