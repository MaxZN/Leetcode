#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def DFS(root):
            if not root:
                return 0
            #如果是左子树为左叶子节点，答案为左叶子数值加上右子树答案
            if root.left and not root.left.left and not root.left.right:
                return  DFS(root.right) + root.left.val
            # 否则，答案为左右子树答案之和
            return DFS(root.left) + DFS(root.right) 
        return DFS(root)

# @lc code=end

