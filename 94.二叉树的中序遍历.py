#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        left, mid, right = [], [], []
        if root.left is not None:
            left = self.inorderTraversal(root.left)
        mid = [root.val]
        if root.right is not None:
            right = self.inorderTraversal(root.right)
        return left + mid + right
# @lc code=end

