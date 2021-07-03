#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None or len(nums)==0:
            return None
        size = len(nums)
        if size==1:
            return TreeNode(nums[0])
        head = TreeNode(nums[size//2])
        left_nums, right_nums = self.split(nums)
        head.left = self.sortedArrayToBST(left_nums)
        head.right = self.sortedArrayToBST(right_nums)
        return head

    def split(self, nums):
        size = len(nums)
        mid = size//2
        left_nums = nums[:size//2]
        if size//2 + 1 == len(nums):
            right_nums = []
        else:
            right_nums = nums[size//2+1:]
        return left_nums, right_nums




# @lc code=end

