class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)

        while r <= len(s2):
            subs = s2[l:r]
            if sorted(subs) == sorted(s1):
                return True
            else:
                l+=1
                r+=1
        
        return False

