class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for num in nums:
            if num in occ.keys():
                occ[num] = occ[num]+1
            else:
                occ[num] =0

            
        return [num for (num, oc) in sorted(list(occ.items()),reverse=True, key=lambda item: item[1])[0:k]]


        
        