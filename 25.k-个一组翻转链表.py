#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head
        cnt = 0
        while right:
            cnt += 1
            right = right.next
            if cnt % k == 0:
                left = self.reverse(left, right)
        return dummy.next
    
    def reverse(self, left, right):
        pre, cur = left, left.next
        first, last = pre, cur
        while cur != right:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        first.next = pre
        last.next = right
        return last


# @lc code=end

