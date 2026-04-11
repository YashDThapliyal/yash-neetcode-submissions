class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            else:
                tmp = 0
                while n != 0:
                    tmp += (n%10)**2
                    n//=10
                    seen.add(n)
                
                n = tmp
        return True
