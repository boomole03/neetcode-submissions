# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            # this will have the currenmt values in the current level?
            level_size = len(queue)
            print('Queue: ', queue, ' level_size: ', level_size)
            for i in range(level_size):
                node = queue.popleft()

                # If it's the last node of this level, add it to the result
                if i == level_size - 1:
                    result.append(node.val)

                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result