#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path = []
        all = []
        def DFS(root):
            if not root:
                return
            else:
                path.append(str(root.val))
                if not root.left and not root.right:
                    all.append('->'.join(path))
                DFS(root.left)
                DFS(root.right)
                path.pop()
        
        DFS(root)
        return all



# @lc code=end

