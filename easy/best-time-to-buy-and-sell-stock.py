class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = {}
        for i, price in enumerate(prices[:-1]):
            profits[i] = max((value, index) for index, value in enumerate(prices[i:]))
        return max(profits[i][0] for i in profits.keys())