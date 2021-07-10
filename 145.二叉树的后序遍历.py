#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        left, mid, right = [], [], []
        if root.left is not None:
            left = self.postorderTraversal(root.left)
        mid = [root.val]
        if root.right is not None:
            right = self.postorderTraversal(root.right)
        return left  + right + mid
# @lc code=end

