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
            arr.append(temp.val)
            temp = temp.next

        n = len(arr)
        temp = head
        i = 0
        j = 0
        while temp:
            if i % 2 == 0:
                temp.val = arr[j]
                i += 1
                j += 1
                temp = temp.next
            else:
                temp.val = arr[n - j]
                i += 1
                temp = temp.next