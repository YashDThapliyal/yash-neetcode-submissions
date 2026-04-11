class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        differences = [0]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                differences.append(prices[j] -prices[i])
    
        return max(differences)