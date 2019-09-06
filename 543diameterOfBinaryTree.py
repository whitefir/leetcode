# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def travel(root):
            if not root:
                return 0
            return max(travel(root.left),travel(root.right))+1
        
        if not root:
            return 0
        return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right),travel(root.right)+travel(root.left))
