class Solution:
    def mergeAlternately(self, str1: str, str2: str) -> str:
        res = ""

        while str1 and str2:
            res+=str1[0]
            res+=str2[0]

            if str1 and str2:
                str1 = str1[1:]
                str2 = str2[1:]
        
        if str1:
            res+=str1
        if str2:
            res+=str2
        
        return res
        

