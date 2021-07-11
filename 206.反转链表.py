#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class BiListNode:
    def __init__(self, val=0, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur,pre = head,None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre        

# @lc code=end

