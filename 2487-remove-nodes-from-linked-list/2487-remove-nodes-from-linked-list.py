# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(head):
            prev = None
            current = head
            next_temp = None

            while current:
                next_temp = current.next
                current.next = prev
                prev = current
                current = next_temp

            return prev
    
        head = reverse_list(head)

        maximum = 0
        prev = None
        current = head

        while current:
            maximum = max(maximum, current.val)

            if current.val < maximum:
                prev.next = current.next
                deleted = current
                current = current.next
                deleted.next = None
            else:
                prev = current
                current = current.next
        
        return reverse_list(head)