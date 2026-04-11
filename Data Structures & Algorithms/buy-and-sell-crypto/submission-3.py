class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        max_prof = 0

        while right< len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_prof = max(max_prof, profit)
    
            else:
                left = right
            
            right+=1
        
        return max_prof
        # differences = [0]
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         differences.append(prices[j] -prices[i])
    
        # return max(differences)