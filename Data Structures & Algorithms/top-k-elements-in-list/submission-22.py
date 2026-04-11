class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.defaultdict(int)
        freq = [[] for i in range(0, len(nums)+1)]
        res = []
        # [1,2,2,3,3,3]

        for n in nums:
            counts[n] = 1 + counts[n]
        
        for num, count in counts.items():
            freq[count].append(num)
        

        for i in range(len(freq)-1, -1,-1):
            if len(freq[i]) != 0:
                for number in freq[i]:
                    res.append(number)
                    if len(res) == k:
                        return res
            
        