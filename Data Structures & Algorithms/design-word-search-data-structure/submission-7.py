class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
       self.storage = [] 
       self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        #self.storage.append(word)

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0,self.root)


        #do a linear search O(n)
        # for curr in self.storage:
        #     if len(curr) != len(word):
        #         continue

        #     i = 0
        #     while i < len(word):
        #         if curr[i] == word[i] or word[i] == ".":
        #             i+=1
        #         else:
        #             break
            
        #     if i == len(word):
        #         return True
            
        # return False


