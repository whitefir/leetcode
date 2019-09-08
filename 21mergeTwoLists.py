# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not(l1 or l2):
            return None
        l3=ListNode(0)
        head=l3
        while(l1 and l2):
            if l1.val<=l2.val:
                l3.val=l1.val
                l1=l1.next
            else:
                l3.val=l2.val
                l2=l2.next
            l3.next=ListNode(0)
            l3=l3.next
        if l1:
            l3.val=l1.val
            l3.next=l1.next
        elif l2:
            l3.val=l2.val
            l3.next=l2.next
        else:
            l3=None
        return head
