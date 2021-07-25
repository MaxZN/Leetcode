#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        node = [root]
        out = []
        if root is None: return out
        while node:
            tmpnode = node.pop()
            out.append(tmpnode.val)
            if tmpnode.children is not None:
                for child in tmpnode.children[::-1]:
                    node.append(child)
        return out
        
# @lc code=end

