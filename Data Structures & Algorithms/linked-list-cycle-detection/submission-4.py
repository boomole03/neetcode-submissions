# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        1 -> 2 -> 3 -> 4
             ^         |
             <----------

        slow = 1 -> 2 -> 3 -> 4
        fast = 1 -> 3 -> 2 -> 4 #match

        """
        
        if not head:
            return False

        slow = fast = head

        while fast.next and fast.next.next:
            if slow == fast.next: 
                return True
            slow = slow.next
            fast = fast.next.next

        return False

    