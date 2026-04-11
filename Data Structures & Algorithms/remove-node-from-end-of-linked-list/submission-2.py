# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse the linked list and then remove the nth element from that 

        dummy = ListNode(0, head)  # Dummy node points to the head
        slow = dummy
        fast = dummy
        
        # Move `fast` n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move `slow` and `fast` until `fast` reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next  # Return the head of the updated list
