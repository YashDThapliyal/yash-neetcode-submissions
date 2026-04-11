class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        hold = prices[0]
        for p in prices:
            hold = min(hold, p)
            profit = max(profit, p - hold)
        
        return profit