#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left ==0 and right==0:
            return 1
        elif (left == 0 and right!=0) or (left!=0 and right==0):
            return max(left,right)+1
        else:
            return min(left,right)+1

# @lc code=end

