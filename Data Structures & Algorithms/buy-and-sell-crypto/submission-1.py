class Solution:
    def maxProfit(self, prices):
        profit = 0
        price = float('inf')

        for p in prices:
            price = min(p,price)
            profit = max(profit, p-price)
        return profit