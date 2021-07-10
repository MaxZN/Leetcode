# @before-stub-for-debug-begin
from python3problem172 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <= 0:
            return 0
        fives = []
        i = 1
        while (n // (5**i)) != 0:
            fives.append(n//(5**i))
            i += 1
        
        return sum(fives)
# @lc code=end

