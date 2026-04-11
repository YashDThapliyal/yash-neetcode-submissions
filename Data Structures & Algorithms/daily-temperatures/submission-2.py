class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [index, temp]

        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                currInd, currT = stack.pop()
                res[currInd] = ind - currInd
            stack.append([ind, temp])
        return res

        