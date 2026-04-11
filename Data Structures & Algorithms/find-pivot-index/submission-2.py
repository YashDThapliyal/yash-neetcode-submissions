class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)

        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
                
        
        return -1