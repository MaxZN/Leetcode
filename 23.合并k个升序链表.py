#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode()
        nodelist = []

        for node in lists:
            tmp = node
            while tmp:
                nodelist.append(tmp.val)
                tmp = tmp.next

        nodelist.sort()
        head = dummy
        for val in nodelist:
            tmpnode = ListNode(val)
            head.next = tmpnode
            head = head.next
        
        return dummy.next
    
    def merge(self, a, b):
        dummy = ListNode(-1)
        x = dummy
        while a and b:
            if a.val < b.val:
                x.next = a
                a = a.next
            else:
                x.next = b
                b = b.next
            x = x.next
        if a:
            x.next = a
        if b:
            x.next = b
        return dummy.next

# @lc code=end

