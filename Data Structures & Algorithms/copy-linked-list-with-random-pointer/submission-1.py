"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None
        copy = head

        copy_map = {}
        copy_map[head] = Node(head.val)

        while head:
            # make a copy of the next node
            if head.next not in copy_map:
                # we need to create the node
                copy_map[head.next] = Node(head.next.val) if head.next else None

            copy_map[head].next = copy_map[head.next]


            # make a copy of the random node
            if head.random not in copy_map:
                # we need to create the node
                copy_map[head.random] = Node(head.random.val) if head.random else None
            
            copy_map[head].random = copy_map[head.random]

            head = head.next

        return copy_map[copy]