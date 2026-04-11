class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits))) + 1  
        return [int(ch) for ch in str(num)]     
