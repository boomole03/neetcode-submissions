# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = float('-inf')
        if not root: 
            return m

        def dfs(node):
            nonlocal m
            if not node: 
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            combined_largest = max(0, left) + max(0, right) + node.val
            m = max(m, combined_largest)
            return max(node.val + max(left, right), node.val)

        dfs(root)
        return m