# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        for l in lists:
            temp = l

            while temp:
                res.append(temp.val)
                temp = temp.next

        res.sort()

        dummy = ListNode()
        curr = dummy

        for n in res:
            curr.next = ListNode(n)
            curr = curr.next

        return dummy.next