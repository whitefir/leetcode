# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def traversal(root):
            if root:
                traversal(root.left)
                ans.append(root.val)
                traversal(root.right)
        traversal(root)
        return ans
