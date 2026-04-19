# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if len(lists)==0:
                return None

            dummy=ListNode()
            dummy.next=lists[0]

            for i in range(1, len(lists)):
                tmp = lists[i]
                curr=dummy

                while curr.next and tmp:
                    if curr.next.val < tmp.val:
                        curr=curr.next
                    else:
                        newn=ListNode(tmp.val)
                        newn.next=curr.next
                        curr.next=newn
                        curr=curr.next
                        tmp=tmp.next

                while tmp:
                    newn=ListNode(tmp.val)
                    newn.next=curr.next
                    curr.next=newn
                    curr=curr.next
                    tmp=tmp.next

            return dummy.next