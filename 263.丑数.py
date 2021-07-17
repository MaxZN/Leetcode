#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        res = -1
        while n > 0:
            n = n // 2 if n%2==0 else n
            n = n // 5 if n%5==0 else n
            n = n // 3 if n%3==0 else n
            if n==1:
                return True
            if res == n:
                return False
            res = n
        return False
# @lc code=end

