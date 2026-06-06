# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        traverse down the tree starting at root

        check to see if node is q or p, if return q or p
        else: 
            go futher down, 

        """

        def dfs(node):
            if node: 
                if node is q or node is p:
                    return node

                left = dfs(node.left)
                right = dfs(node.right)

                if left and right:
                    return node
                return left or right

        return dfs(root)
        