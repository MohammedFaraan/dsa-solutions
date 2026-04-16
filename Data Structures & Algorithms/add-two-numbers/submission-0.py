# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        t1 = l1
        t2 = l2

        dummyNode = ListNode(0)
        newList = dummyNode

        carry = 0

        while t1 and t2:
            sum = t1.val + t2.val + carry

            sCarry = str(sum)
            new_n = ListNode()
            if len(sCarry) > 1:
                carry = int(sCarry[0])
                new_n.val = int(sCarry[1])
            else:
                new_n.val = sum
                carry = 0

            t1 = t1.next
            t2 = t2.next
            newList.next = new_n
            newList = newList.next

        while t1:
            sum = t1.val + carry

            sCarry = str(sum)
            new_n = ListNode()

            if len(sCarry) > 1:
                carry = int(sCarry[0])
                new_n.val = int(sCarry[1])
            else:
                new_n.val = sum
                carry = 0

            t1 = t1.next
            newList.next = new_n
            newList = newList.next

        while t2:
            sum = t2.val + carry

            sCarry = str(sum)
            new_n = ListNode()

            if len(sCarry) > 1:
                carry = int(sCarry[0])
                new_n.val = int(sCarry[1])
            else:
                new_n.val = sum
                carry = 0

            t2 = t2.next
            newList.next = new_n
            newList = newList.next

        if carry != 0:
            new_n = ListNode(carry)
            newList.next = new_n
            newList = newList.next

        return dummyNode.next
