class WordDictionary:

    def __init__(self):
       self.storage = [] 

    def addWord(self, word: str) -> None:
        self.storage.append(word)

    def search(self, word: str) -> bool:
        #do a linear search O(n)
        for curr in self.storage:
            if len(curr) != len(word):
                continue

            i = 0
            while i < len(word):
                if curr[i] == word[i] or word[i] == ".":
                    i+=1
                else:
                    break
            
            if i == len(word):
                return True
            
        return False


