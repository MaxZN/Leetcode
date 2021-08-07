#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        start, end = ListNode(), ListNode()
        start.next = head
        end.next = head
        n = 0
        while end.next:
            end = end.next
            n+=1
        end.next = head
        for _ in range(n - k % n):
            start = start.next
        pnode = start.next
        start.next = None
        return pnode

# @lc code=end

