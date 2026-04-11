class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board) 
        cols = len(board[0]) 
        seen = set()

        def dfs(r, c, index):
            
            if r < 0 or r > rows-1:
                return False
            
            if c < 0 or c > cols-1:
                return False
            
            if board[r][c] != word[index]:
                return False
            
            if (r,c) in seen:
                return False

            if board[r][c] == word[index] and index == len(word) -1:
                return True

            seen.add((r,c))
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]
            
            for dr, dc in dirs:
                if dfs(r+dr, c+dc, index+1):
                    return True

            seen.remove((r,c))
            return False

        for r in range(0, rows):
            for c in range(0, cols):
                if dfs(r,c,0):
                    return True
        
        return False

        
