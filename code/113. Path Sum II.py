# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def find_path(root, sum, cur_path, record_path):
            if root == None:
                return

            cur_path.append(root.val)
            target = sum - root.val
            if root.left == None and root.right == None and target == 0:
                record_path.append(list(cur_path))
            find_path(root.left, target, cur_path, record_path)
            find_path(root.right, target, cur_path, record_path)
            cur_path.pop()

        record_path = []
        cur_path = []
        if root == None:
            return record_path
        find_path(root, sum, cur_path, record_path)
        return record_path