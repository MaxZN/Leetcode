#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.vals = []

        # self.inorder(root)
        # self.diffval = [self.vals[i]-self.vals[i-1] for i in range(1,len(self.vals))]
        # print(self.diffval)
        # print(self.vals)
        # return min(self.diffval)

        self.prenodeval = None
        self.minval = 10000000
        self.inordercmp(root)
        return self.minval

    def inorder(self, root):
        if root is None:
            return 
        self.inorder(root.left)
        self.vals.append(root.val)
        self.inorder(root.right)
    
    def inordercmp(self, root):
        if root is None:
            return 
        self.inordercmp(root.left)
        if self.prenodeval is not None:
            self.minval = min(self.minval, root.val-self.prenodeval)

        self.prenodeval = root.val
        self.inordercmp(root.right)




# @lc code=end

