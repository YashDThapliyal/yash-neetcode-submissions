class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        l = 0
        r = 0

        seen = set()
        maxWin = 1
        
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
                
            seen.add(s[r])
            r+=1
            maxWin = max(r-l, maxWin)
        
        return maxWin
