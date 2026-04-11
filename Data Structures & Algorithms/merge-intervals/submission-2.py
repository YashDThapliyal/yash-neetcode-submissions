class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda a: a[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            new_start = intervals[i][0]
            new_end = intervals[i][1]
            
            curr_start = res[-1][0]
            curr_end = res[-1][1]

            if new_start <= curr_end:
                res[-1][1] = max(curr_end,new_end)
            else:
                res.append(intervals[i])
        
        return res