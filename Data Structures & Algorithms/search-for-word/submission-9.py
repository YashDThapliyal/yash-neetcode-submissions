class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def dfs(r,c,idx):
            #bases cases
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            if board[r][c] != word[idx] or (r,c) in visited:
                return False
            
            if idx == len(word) -1 and board[r][c] == word[idx]:
                return True

            visited.add((r,c))
            #now check neighbours

            x = dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c+1, idx+1) or dfs (r, c-1, idx+1)
            
            visited.remove((r,c))

            return x
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        
        return False
                
        

        