#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        dic = [0]*(n+1)
        dic[1] = 1
        for i in range(2,n+1):
            dic[i] = dic[i-1] + dic[i-2]
        return dic[n]
# @lc code=end

