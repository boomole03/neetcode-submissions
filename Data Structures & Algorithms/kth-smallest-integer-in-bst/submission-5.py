# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we can traverse in order
        res = -1
        def dfs(node):
            nonlocal res, k
            if not node: 
                return 0
            
            dfs(node.left)
            k -= 1
            if k == 0: 
                res = node.val
            dfs(node.right)

        dfs(root)
        return res