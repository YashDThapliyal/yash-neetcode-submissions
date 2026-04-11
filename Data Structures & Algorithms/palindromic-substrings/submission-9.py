class Solution:
    def countSubstrings(self, s: str) -> int:
        #count even palindromes
        l, r = 0,0
        count = 0
        for i in range(0, len(s)):
            l = r = i
            while l >=0 and r< len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            
            l = i
            r = i +1
            while l >=0 and r< len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
        
        return count
            


        #count odd palindromes