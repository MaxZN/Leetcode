#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy=ListNode
        dummy.next = head
        cur, nex = head, head.next
        while cur and nex:
            while nex and cur.val==nex.val:
                nex = nex.next
            cur.next = nex
            if nex is None: break
            cur, nex = nex, nex.next
        return dummy.next

# @lc code=end

