#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.cnt = 0
        if root is None: return 0
        def search(head):
            if head is None: return 0
            left_val = search(head.right)
            right_val = search(head.left)
            self.cnt += abs(left_val - \
                right_val)
            return head.val + right_val + left_val
        search(root)
        return self.cnt
# @lc code=end

