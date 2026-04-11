class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #last digit is 9
        if digits[-1] == 9:
            i = len(digits) -1
            while i >= 0 and digits[i] == 9:
                digits[i] = 0
                i-=1
            
            if i <0:
                digits.insert(0,1)
            else:
                digits[i] +=1

        else:    
            #isnt:
            digits[-1]+=1
        return digits