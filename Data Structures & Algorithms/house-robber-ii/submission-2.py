class Solution:
    def rob(self, nums: List[int]) -> int:
        def hr(arr):
            rob1, rob2 = 0,0
            #[rob1, rob2, n, n+1]
            for n in arr:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2

        
        return max(nums[0],hr(nums[1:]), hr(nums[0:len(nums)-1]))

