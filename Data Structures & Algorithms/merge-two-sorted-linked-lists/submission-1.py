# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        arr = []

        temp1 = list1
        temp2 = list2

        while temp1:
            arr.append(temp1.val)
            temp1 = temp1.next

        while temp2:
            arr.append(temp2.val)
            temp2 = temp2.next

        arr.sort()

        head = ListNode(arr[0])
        temp = head

        for i in range(1, len(arr)):
            new_n = ListNode(arr[i])
            temp.next = new_n
            temp = temp.next

        return head
