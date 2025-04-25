# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        next_node = head.next
        first_node = ListNode(head.val, None)
        index_node = first_node
        
        while next_node:
            if index_node.val != next_node.val:
                index_node.next = ListNode(next_node.val, None)
                index_node = index_node.next

            next_node = next_node.next

        return first_node