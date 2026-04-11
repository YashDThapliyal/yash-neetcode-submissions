class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        res = [1] * n
        for i in range(0, len(nums)):
            res[i] = res[i] * prefix
            prefix = prefix * nums[i]

            res[n-1-i] = res[n-1-i] * suffix
            suffix = suffix * nums[n-1-i]
        
        return res
