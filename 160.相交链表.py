#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        # if co-node exists, then must achieve same end-node
        # else, till the-end None=None
        while a != b:
            if a:
                a = a.next 
            else:
                a = headB

            if b:
                b = b.next
            else:
                b = headA
            
        return a

        
# @lc code=end

