class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        finalNum = ""
        for ch in digits:
            finalNum += (str(ch))

        s = int(finalNum)+1
        
        res = []
        for ch in str(s):
            res.append(int(ch))

        return res