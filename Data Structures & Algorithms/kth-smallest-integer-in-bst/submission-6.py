class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = -1
        cnt = 0
        def dfs(node):
            nonlocal cnt, res
            if not node or res != -1:
                return

            dfs(node.left)
            cnt += 1
            if cnt == k:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res