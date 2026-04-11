class Solution:
    def isPalindrome(self, s: str) -> bool:
        #filtr input 
        #x: str.isalnum(x))(s)
        word = [charac.lower() for charac in s if str.isalnum(charac)]
        print(word)
        for i in range(len(word)):
            if word[i] != word[len(word)-i-1]:
                return False
            
        return True




                             
        