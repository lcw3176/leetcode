# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        node = None
        first = None
        
        if head.val == val:
            while True:
                if head.val != val:
                    node = ListNode(val=head.val)
                    first = node
                    break

                head = head.next

                if not head:
                    break
            
            if not node:
                return None

        node = ListNode(val=head.val)
        first = node
        head = head.next

        if not head:
            return first

        while True:
            if head.val != val:
                temp = ListNode(val=head.val)
                node.next = temp
                node = node.next
            
            head = head.next

            if not head:
                break

        return first