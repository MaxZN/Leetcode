#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1

        half = n
        while half*(half+1) > n*2:
            half = half // 2
        print(half)
        for i in range(half, half*2+2):
            if i*(i+1) > n*2:
                return i-1
# @lc code=end

