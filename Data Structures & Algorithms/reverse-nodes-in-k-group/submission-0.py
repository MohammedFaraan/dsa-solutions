# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []

        temp = head

        while temp:
                nums.append(temp.val)
                temp = temp.next

                                                            
        n = len(nums)
        for i in range(0, n, k):
                if i + k > n:
                        break

                nums[i : i + k] = nums[i : i + k][::-1]
                                                                                                                                

        dummy = ListNode()
        tail = dummy
        
        for n in nums:
                tail.next = ListNode(n)
                tail = tail.next
        
        return dummy.next

                                                                                                                                                                                             