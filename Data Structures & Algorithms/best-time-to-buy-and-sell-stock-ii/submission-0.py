class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in prices:
            if i < buy:
                buy = i
            if i > buy:
                profit = i - buy
                max_profit += profit
                buy = i
        return max_profit
        