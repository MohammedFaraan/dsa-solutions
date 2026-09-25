# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            res = str(v1 + v2 + carry)
            if len(res) > 1:
                carry = int(res[0])
                res = int(res[1])
            else:
                carry = 0
                res = int(res)

            temp.next = ListNode(res)
            temp = temp.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry:
            temp.next = ListNode(carry)

        return dummy.next
