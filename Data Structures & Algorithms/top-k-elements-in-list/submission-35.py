class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        
        print(nums)
        for n in nums:
            d[n] += 1
        
        sd = sorted(d.items(), key=lambda x: x[1], reverse=True)[0:k]
        result = [num for num, freq in sd]
        return result
