class Solution:
    def isPalindrome(self, s: str) -> bool:
        # r a c e c a r
        # 0 1 2 3 4 5 6    

        #filter s for alphanumeric
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s+=c.lower()
        
        return new_s == new_s[::-1]            
        