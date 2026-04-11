class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lSum = 0

        for i in range(len(nums)):
            if lSum == total - lSum - nums[i]:
                return i
            lSum+=nums[i]
                
        
        return -1