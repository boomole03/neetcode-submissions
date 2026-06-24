"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None

        # keep a map of the clone nodes
        cloned_map = {}

        # clone the intial node
        cloned_map[node] = Node(val=node.val)
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in cloned_map:
                    cloned_map[nei] = Node(val=nei.val)
                    queue.append(nei)
                cloned_map[curr].neighbors.append(cloned_map[nei])

        return cloned_map[node]


        