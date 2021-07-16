#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        prev = None
        flag = True
        # step1: reverse
        while(fast and fast.next):
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # step2: compare
        if fast: # 奇数
            node1 = prev
            node2 = slow.next
        else: # 偶数
            node1 = prev
            node2 = slow
        while(node1 and node2):
            if node1.val != node2.val:
                flag = False
            node1, node2 = node1.next, node2.next
        # # step3: recover(optional)
        # back = slow
        # while(prev):
        #     temp = prev.next
        #     prev.next = back
        #     back = prev
        #     prev = temp
        return flag


# @lc code=end

