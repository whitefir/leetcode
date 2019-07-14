# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA:ListNode, headB:ListNode)->ListNode:
        pA,pB=headA,headB
        while pA.val!=pB.val:
            pA=pA.next if pA.next else headB
            pB=pB.next if pB.next else headA
            if pA==None and pB==None:
                return None
        return pA
