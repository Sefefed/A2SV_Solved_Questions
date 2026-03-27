from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.pathSums = defaultdict(int)
        self.pathSums[0] = 1
        def dfs(node, currSum):
            if not node:
                return 
            currSum += node.val
            self.paths += self.pathSums[currSum - targetSum] 
            self.pathSums[currSum] += 1

            if node.left:
                dfs(node.left, currSum)
            if node.right:
                dfs(node.right, currSum) 
            self.pathSums[currSum] -= 1
        dfs(root, 0)      
        return self.paths     



        
