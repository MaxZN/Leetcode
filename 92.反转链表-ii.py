#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:       
        cnt = 1
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while pre and cnt<left:
            pre = pre.next
            cnt += 1
        cur = pre.next
        tail = cur

        while cur and cnt <= right:
            nxt = cur.next
            cur.next = pre.next
            pre.next = cur
            tail.next = nxt
            cur = nxt
            cnt += 1
        return dummy.next

# @lc code=end

