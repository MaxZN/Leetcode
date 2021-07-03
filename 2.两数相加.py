#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:s
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        head = res
        push = 0
        while (l1 or l2):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            added = push + v1 + v2
            new = ListNode(added % 10)
            head.next = new
            head = head.next
            push = 1 if (added > 9) else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if push==1:
            head.next = ListNode(1)

        return res.next


# @lc code=end

