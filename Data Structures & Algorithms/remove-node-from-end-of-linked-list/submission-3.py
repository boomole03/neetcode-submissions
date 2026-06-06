# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        dummy = ListNode(-1, head)

        curr = head
        for _ in range(n):
            curr = curr.next

        prev = dummy
        rem = head
        while curr:
            prev = rem
            rem = rem.next
            curr = curr.next

        prev.next = rem.next


        return dummy.next