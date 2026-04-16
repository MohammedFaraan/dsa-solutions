# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def insert_end(head, val):
    new_n=ListNode(val)

    if head is None:
        head = new_n
        return head
    
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new_n

    return head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        temp1 = list1
        temp2 = list2

        while temp1 and temp2:
            if temp1.val == temp2.val:
                head=insert_end(head, temp1.val)
                head=insert_end(head, temp2.val)
                temp1=temp1.next
                temp2=temp2.next
            elif temp1.val<temp2.val:
                head=insert_end(head, temp1.val)
                temp1=temp1.next
            else:
                head=insert_end(head, temp2.val)
                temp2=temp2.next
        
        while temp1:
            head=insert_end(head, temp1.val)
            temp1=temp1.next
        
        while temp2:
            head=insert_end(head, temp2.val)
            temp2=temp2.next
        
        return head