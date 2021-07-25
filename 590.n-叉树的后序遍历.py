#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        node = [root]
        out = []
        if root is None: return out
        while node:
            tmpnode = node.pop()
            out.append(tmpnode.val)
            if tmpnode.children is not None:
                for child in tmpnode.children:
                    node.append(child)
        return out[::-1]
# @lc code=end

