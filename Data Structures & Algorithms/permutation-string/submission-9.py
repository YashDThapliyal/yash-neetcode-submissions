class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # l = 0
        # r = len(s1)
        # while r <= len(s2):
        #     subs = s2[l:r]
        #     if sorted(subs) == sorted(s1):
        #         return True
        #     else:
        #         l+=1
        #         r+=1
        
        # return False

        #TC: 0(n^2)
        #SC: o(1)

        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
