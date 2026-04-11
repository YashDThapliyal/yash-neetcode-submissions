class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        maxLen = 0
        l =0
        r = 0
        while l < len(s) and r < len(s):
            if not (s[r] in seen):
                seen.add(s[r])
                maxLen= max(r-l+1, maxLen)
                r+=1
                
            else:
                #while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
        return maxLen



        