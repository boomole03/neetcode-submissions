# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        take 2 list and return them merged in order

        """
        dummy = tail = ListNode()
        while list1 and list2: 
            # while we still have a valid node for both lists we should try and find the correct order
            if list1.val <= list2.val: 
                # take list1
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # if we have valid nodes in list1 or list2 append to the end
        tail.next = list1 or list2
    
        return dummy.next