class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cache = {}

        def backtrack(idx, currList, currSum ):
            #base cases
            if currSum == target:
                res.append(currList.copy())
                return
            if currSum > target:
                return
            if idx == len(nums):
                return
            
            #recursive case
            currList.append(nums[idx])
            backtrack(idx, currList, currSum +nums[idx])
            currList.pop()
            backtrack(idx+1, currList, currSum)



        backtrack(0,[],0)
        return res       
