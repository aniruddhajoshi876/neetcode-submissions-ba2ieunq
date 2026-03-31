class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1,len(prices)):
            buy = min(prices[:i])
            profit = max(prices[i]-buy, profit)
        return profit
