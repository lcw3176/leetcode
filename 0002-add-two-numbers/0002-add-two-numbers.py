# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        lst_one = []

        while True:
            lst_one.append(str(node.val))
            node = node.next

            if not node:
                break
        
        node_two = l2
        lst_two = []

        while True:
            lst_two.append(str(node_two.val))
            node_two = node_two.next

            if not node_two:
                break

        lst_one.reverse()
        lst_two.reverse()

        one = int("".join(lst_one))
        two = int("".join(lst_two))
        lst = list(str(one + two))
        lst.reverse()

        answer = ListNode()
        first = answer

        for i in range(len(lst)):
            answer.val = int(lst[i])

            if i < len(lst) - 1:
                answer.next = ListNode()
                answer = answer.next

        return first 
            