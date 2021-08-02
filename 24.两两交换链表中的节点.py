#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        init = ListNode(0)
        init.next = head
        tmp = init
        while tmp.next and tmp.next.next:
            node1 = tmp.next
            node2 = tmp.next.next
            node3 = tmp.next.next.next
            tmp.next = node2
            node2.next = node1
            node1.next = node3
            tmp = node1
        return init.next



# @lc code=end

