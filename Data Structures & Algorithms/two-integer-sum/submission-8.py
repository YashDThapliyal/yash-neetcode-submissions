class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3 4 5 6
        # 0 1 2 3

        """
            0: 7-3 = 4
            1: 7-4 = 3
            2: 7-5 = 2
            3: 7-6 = 1
        """

        diffs = {}
        for i in range(0, len(nums)):
            curr_dif = target - nums[i]
            if curr_dif in diffs:
                return [diffs[curr_dif],i]
            else:
                diffs[nums[i]] = i
            