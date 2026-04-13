class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        m1 = {}
        m2 = {}


        for l in s:
            m1[l] = m1.get(l,0) + 1

        for l in t:
            m2[l] = m2.get(l,0)+1
        
        return m1 == m2
