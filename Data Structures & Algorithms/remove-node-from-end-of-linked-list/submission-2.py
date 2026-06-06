# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1 -> 2 -> 3 -> 4 (remove n = 2)
        1 -> 2 -> B -> 4

        """
        dummy = ListNode(0, head)
        mark = head

        for _ in range(n):
            mark = mark.next

        # find thing to remove
        r = head
        prev = dummy
        while mark: 
            mark = mark.next
            prev = r
            r = r.next

        prev.next = r.next


        return dummy.next
