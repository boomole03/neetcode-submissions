# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        we can use a heap maybe to figure this out? max heap with only maintian k len characters

        we need to exhuast the left side first 
            - the lowest value going to the left first will be the 1st k and then right would be the 2nd k

        """

        count = k
        res = root.val
        def dfs(node):
            nonlocal count, res
            if not node:
                return 


            dfs(node.left)
            count -= 1
            if count == 0: 
                res =  node.val
                return
            dfs(node.right)

        dfs(root)
        return res