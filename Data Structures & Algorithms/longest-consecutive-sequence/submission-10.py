class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        bestCounter = 0
        counter = 0
        for num in nums:
            if num -1 not in nums:
                #new sequence
                curr = num
                while curr+1 in nums:
                    curr+=1
                    counter+=1
                bestCounter = max(bestCounter, counter)
                counter = 0

        return bestCounter+1
