# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        root1 = p
        root2 = q
        verified = True
        def check(root1, root2):
            nonlocal verified
            if not root1 and not root2:
                return
            if root1 and root2 and root1.val != root2.val or (root1 and not root2) or (root2 and not root1):
                verified = False
                return 
            check(root1.left, root2.left)
            check(root1.right, root2.right)    
        check(root1, root2)
        return verified    
