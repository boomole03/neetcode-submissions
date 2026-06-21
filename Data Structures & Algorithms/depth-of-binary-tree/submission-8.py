# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bottom - up approach
        # child sends depth to parent

        def dfs(node):
            if not node: 
                return 0

            # get the depth for child
            left = dfs(node.left)
            right = dfs(node.right)

            # return that depth to the parent
            return 1 + (max(left, right))
        return dfs(root)