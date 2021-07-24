#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dicts = {}

        ##使用DFS来整一遍
        def dfs(root):
            if not root:
                return 
            if root.val not in dicts:
                dicts[root.val] = 1
            else:
                dicts[root.val]+=1
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print(dicts)
        maxVal = max(dicts.values())
        ans = []
        for item,val in dicts.items():
            if val>=maxVal:
                ans.append(item)
        return ans


# @lc code=end

