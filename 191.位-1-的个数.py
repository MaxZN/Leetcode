#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        count = 0
        while n != 1:
            remainder = n % 2
            n = n // 2
            if remainder == 1:
                count += 1
        return count + 1

# @lc code=end

