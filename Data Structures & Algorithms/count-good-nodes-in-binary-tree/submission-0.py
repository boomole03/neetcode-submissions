# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        queue = deque([(root, float('-inf'))])

        while queue: 
            for _ in range(len(queue)):
                n, m = queue.popleft()
                if n.val >= m:
                    res += 1
                
                if n.left:
                    queue.append((n.left, max(m, n.val)))
                if n.right:
                    queue.append((n.right, max(m, n.val)))
                
        return res