class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #start at day 0 for buy 
        #start at day 1 for sell 

        #calcluate profit by doing sell - buy 
        #if prices[i] < buy --> update buy to = prices[i] (buying at a low)
        #if prices[i] > sell --> update sell to prices[i] (selling at a high )

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r

            r+=1

        return maxP