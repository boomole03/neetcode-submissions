# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        to find the middle let's use the slow and fast pointer

        1 -> 2 -> 3 -> 4 -> 5
                  s
                            f

        when it's even
        1 -> 2 -> 3 -> 4 -> 5 -> 6
                  s
                            f
        """
        if not head:
            return None

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow