#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:return False
        res = -1
        while n>1:
            if n%3==0:
                n = n//3
            if n==1: return True
            if n==res: return False
            res = n
        return True
# @lc code=end

