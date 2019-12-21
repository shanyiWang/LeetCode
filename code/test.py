
'''
给定一棵二叉树，两个节点间的路径和定义为连通两个节点的路径上所有节点值之和，例如a，b两个节点连通路径上有c和d，ab的路径和就等于a.val+c.val+d.val+b.val。求二叉树中最大的路径和
'''
def find_max_val(root):
    record_max = 0
    def find_max(root, record_max):
        if root.left == None and root.right == None:
            return root.val
        left_val = find_max(root.left, record_max)
        right_val = find_max(root.rigt, record_max)
        sum_val = left_val + right_val + root.val
        if sum_val > record_max:
            record_max = sum_val
        return max(left_val + root.val, right_val + root.val)

    if root == None:
        return 0
    if root.left == None and root.right == None:
        return root.val
    find_max(root, record_max)
    return record_max
