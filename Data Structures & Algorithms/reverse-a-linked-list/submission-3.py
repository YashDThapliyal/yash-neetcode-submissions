# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        # null -> 0 -> 1 -> 2
        # null <- 0 <- 1 <- 2        
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev