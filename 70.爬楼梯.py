#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        solu = [0, 1, 2]
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            for i in range(3, n+1):
                solu.append(solu[i-1]+solu[i-2])
            return solu[n]
# @lc code=end

