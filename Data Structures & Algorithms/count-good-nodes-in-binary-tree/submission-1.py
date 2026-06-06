# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, m=float('-inf')):
            if not node: 
                return
            # print('Node: ', node.val, ' max: ', m)
            if node.val >= m:
                self.count +=1
                print('Node: ', node.val)
                m = node.val

            left = dfs(node.left, m)
            right = dfs(node.right, m)


        dfs(root)
        return self.count