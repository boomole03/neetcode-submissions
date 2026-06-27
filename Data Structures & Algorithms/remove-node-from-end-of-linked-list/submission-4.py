# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f_node = head
        dummy = ListNode(next=head)
        for _ in range(n):
            f_node = f_node.next
        """
        1 -> 2 -> 3 -> 4
                       f
              p   n
        """
        prev, nth_node = dummy, head
        while f_node:
            prev = nth_node
            nth_node = nth_node.next
            f_node = f_node.next


        # now remove the nth_node
        """
             - - - - - -
             |         | 
        1 -> 2 -> 3 -> 4
             p    n
            
        """
        prev.next = nth_node.next
        return dummy.next
