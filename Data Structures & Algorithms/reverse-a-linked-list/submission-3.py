# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 -> 2 -> 3 -> 4 -> 5
        initial:
        prev = None
        curr = head
        
        recursive: 
        next = curr.next # store the next node
        curr.next = prev # move pointed on curr to previous 
        prev = curr
        curr = next

        1 <- 2 <- 3 <- 4 <- 5
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next # store the next node
            curr.next = prev # move pointed on curr to previous 
            prev = curr
            curr = nxt
        return prev
        