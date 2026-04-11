# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse the linked list and then remove the nth element from that 
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        new_head = prev  # Head of the reversed list

        # Step 2: Remove the nth node from the reversed list
        dummy = ListNode(0, new_head)  # Dummy node to simplify removal logic
        curr = dummy
        for _ in range(n - 1):
            curr = curr.next
        
        # Remove the nth node
        curr.next = curr.next.next if curr.next else None

        # Step 3: Reverse the list back to restore the original order
        prev = None
        curr = dummy.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev  # Return the head of the restored list
