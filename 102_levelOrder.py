# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return[]
        queue=[root]
        ans=[]
        
        while(queue):
            nodes=[]
            child=[]
            for i in queue:
                nodes.append(i.val)
                if i.left:
                    child.append(i.left)
                if i.right:
                    child.append(i.right)
            ans.append(nodes)
            queue=child
        return ans
        
