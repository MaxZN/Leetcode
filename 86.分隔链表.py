#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        small = ListNode()
        sm = small
        large = ListNode()
        lg = large
        while head:
            if head.val < x:
                sm.next = head
                sm = sm.next
            else:
                lg.next = head
                lg = lg.next
            head = head.next
        lg.next = None
        sm.next = large.next
        return small.next

# @lc code=end

