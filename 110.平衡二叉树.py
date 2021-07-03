#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = self.HeightCal(root.left)
        right = self.HeightCal(root.right)
        if abs(left-right)<=1  and \
            self.isBalanced(root.left) and \
                self.isBalanced(root.right):
            return True
        return False
        
    def HeightCal(self, root):
        if root is None:
            return 0
        return 1 + max(self.HeightCal(root.right), \
                       self.HeightCal(root.left))
# @lc code=end

