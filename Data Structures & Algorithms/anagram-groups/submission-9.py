class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            words[sorted_word].append(word)

        return list(words.values())