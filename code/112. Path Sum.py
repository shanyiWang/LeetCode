# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        target = sum-root.val
        if root.left == None and root.right == None and target == 0:
            return True
        left = self.hasPathSum(root.left, target)
        right = self.hasPathSum(root.right, target)
        return left or right