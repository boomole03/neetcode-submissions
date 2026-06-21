# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # top - down approach, parent needs to give the child the largest in that path so far
        good_nodes = 0

        def dfs(node, largest):
            nonlocal good_nodes

            if not node:
                return 

            if node.val >= largest: 
                good_nodes += 1

            largest = max(largest, node.val)
            dfs(node.left, largest)
            dfs(node.right, largest)


        dfs(root, float('-inf'))
        return good_nodes