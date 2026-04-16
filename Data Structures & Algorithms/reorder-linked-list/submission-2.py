# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
            
        nodes = []

        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        temp = head
        i = 0
        j = len(nodes)-1

        while i < j:
            nodes[i].next = nodes[j]
            i+=1

            if i >= j:
                break
            nodes[j].next = nodes[i]
            j-=1
        
        nodes[i].next = None
