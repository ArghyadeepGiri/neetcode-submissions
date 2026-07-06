class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = prices[0]
        max_profit = 0
        profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - lowest_buy
            lowest_buy = min(prices[i], lowest_buy)
            profit = max(max_profit, profit)
            max_profit = profit
        return profit