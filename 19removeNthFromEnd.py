# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast,slow =head, head
        for i in range(n):
            fast=fast.next    
        if fast is None: return head.next if head else head
        
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head
