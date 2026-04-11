class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #hash map for frequencies, then whcihever one isn't 1 we return 

        counts = Counter(nums)

        for key,val in counts.items():
            if val != 1:
                return key