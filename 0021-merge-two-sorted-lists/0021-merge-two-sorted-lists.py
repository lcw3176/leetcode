# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        node = list1

        while node:
            val = node.val
            node = node.next

            lst.append(val)
            
        
        node2 = list2

        while node2:
            val = node2.val
            node2 = node2.next

            lst.append(val)

        lst.sort()

        if len(lst) == 0:
            return 

        now = ListNode()
        first = now 

        for i in range(0, len(lst)):
            now.val = lst[i]

            if i < len(lst) - 1:
                now.next = ListNode()

            now = now.next

        return first

        