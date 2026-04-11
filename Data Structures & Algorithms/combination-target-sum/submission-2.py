class Solution:
    def combinationSum(self, canidates: List[int], target: int) -> List[List[int]]:
        
        #Case 1: include current value 
        #Case 2: don't include current value 
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(canidates) or total> target:
                return 
            
            
            cur.append(canidates[i])
            dfs(i, cur, total + canidates[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0,[],0)
        return res
            