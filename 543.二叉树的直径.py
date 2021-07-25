#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.dlen = 1
        def search(head):
            if head is None:
                return 0
            left_len = search(head.left)
            right_len = search(head.right)
            max_len = max(left_len, right_len) + 1
            self.dlen = max(self.dlen, left_len+right_len+1)
            return max_len
        max_len = search(root)
        return self.dlen - 1


# @lc code=end

