class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            n = self.sum_square_of_digits(n)
            if n in seen:
                return False
            seen.add(n)

        return True

    def sum_square_of_digits(self, n):
        if n<10:
            return n*n
        else:
            
            summer = 0
            while n > 0:
                summer += (n%10)**2
                n = n//10
            
            return summer