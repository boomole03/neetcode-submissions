# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        [0, 1, 2, 3, 4, 5, 6] -> [0, 6, 1, 5, 2, 4, 3]
        
        1) Find the mid way
        [0, 1, 2, 3, 4, 5, 6]
                  s
                           f
        2) Reverse the second half
        3) Combine them
        """
        
        # finding the mid way
        slow = fast = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # slow is the mid
        prev = None
        curr = second
        while curr:
            tmp = curr.next
            curr.next= prev
            prev = curr
            curr = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

