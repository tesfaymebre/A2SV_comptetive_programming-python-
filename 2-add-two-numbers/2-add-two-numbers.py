# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        
        new_val = l1.val + l2.val + carry
        carry = new_val //10
            
        new_node = ListNode(new_val % 10)
        head = new_node
        curr = head
        l1 = l1.next
        l2 = l2.next
        
        while l1 and l2:
            
            new_val = l1.val + l2.val + carry
            carry = new_val //10
            
            new_node = ListNode(new_val % 10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            
            new_val = l1.val + carry
            carry = new_val //10
            
            new_node = ListNode(new_val % 10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next
        while l2:
            
            new_val = l2.val + carry
            carry = new_val //10
            
            new_node = ListNode(new_val % 10)
            curr.next = new_node
            curr = new_node
            l2 = l2.next
            
        if carry == 1:
            new_node = ListNode(carry)
            curr.next = new_node
            curr = new_node
    
        return head
            
        
       