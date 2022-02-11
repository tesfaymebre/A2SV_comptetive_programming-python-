# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return list1
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        
        new_node = ListNode()
        temp = ListNode()
        
        if list1.val < list2.val:
            new_node = list1
            list1 = list1.next
        else:
            new_node = list2
            list2 = list2.next
            
        temp = new_node
        
        while list1 and list2:
            
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
                
            temp = temp.next
            
        if list1:
            temp.next = list1
            
        if list2:
            temp.next = list2
            
        return new_node
        