# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3= ListNode(0)
        curr=l3
        
        while l1 or l2:
            val1= l1.val if l1 else 0
            val2= l2.val if l2 else 0
            val3= val1+ val2+ curr.val
            curr.val= val3%10
            curr.next= ListNode(val3//10)
            
            if l1: l1=l1.next
            if l2: l2=l2.next
                
            if l1 or l2:
                curr=curr.next
            elif val3<10:
                curr.next= None
            
        return l3
