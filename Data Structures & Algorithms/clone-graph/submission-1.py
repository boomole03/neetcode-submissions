"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        clone_map = {}
        clone_map[node] = Node(val=node.val)
        curr = node
        
        def clone_graph(n):
            if n: 
                for child in n.neighbors:
                    if child not in clone_map:
                        clone_map[child] = Node(val=child.val)
                        clone_graph(child)
                    clone_map[n].neighbors.append(clone_map[child])
            return
        clone_graph(curr)
        return clone_map[node]
