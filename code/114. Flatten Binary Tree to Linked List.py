# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)

        if root.left == None:
            return None
        node = root.left
        while node.right != None:
            node = node.right
        node.right = root.right
        root.right = root.left
        root.left = None