# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_depth = 0
        self.dfs(root, 1)
        return self.max_depth
        
    def dfs(self, node, depth):

        if not node:
            return
        self.max_depth = max(depth, self.max_depth)
        self.dfs(node.left, depth +1)
        self.dfs(node.right, depth +1)

        