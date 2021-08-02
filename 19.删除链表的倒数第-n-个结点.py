#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = right = head
        node_num = 0
        while node_num<n:
            right = right.next
            node_num += 1
        # check if node_num == n
        if right is None: return head.next
        while right.next is not None:
            right = right.next
            left = left.next
        if left.next:
            left.next = left.next.next
        return head
# @lc code=end

