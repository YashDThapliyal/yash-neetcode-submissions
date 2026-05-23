class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        mapS = defaultdict(int)
        mapT = defaultdict(int)

        for c in s:
            mapS[c] += 1

        for c in t:
            mapT[c] += 1

        return mapT == mapS
