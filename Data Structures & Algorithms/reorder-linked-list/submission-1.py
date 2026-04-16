# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []

        temp = head
        while temp:
            arr.append(temp)
            temp = temp.next

        mid = len(arr) // 2
        stack = arr[mid:]

        temp = head
        i = 1
        j = 1

        for i in range(1, len(arr)):
            if (i % 2 != 0) and stack:
                temp.next = stack.pop()
                temp.next.next = None
                temp = temp.next
            else:
                temp.next = arr[j]
                temp.next.next = None
                j += 1
                temp = temp.next
