#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        if left is None and right is None: return True
        if left is None or right is None: return False
        if left.val!=right.val: return False
        check_edge = self.dfs(left.left, right.right)
        check_mid = self.dfs(left.right, right.left)
        return check_edge and check_mid
        

# @lc code=end

