# @before-stub-for-debug-begin
from python3problem171 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        size = len(columnTitle)
        whole = 0
        for i in range(size):
            stri = columnTitle[i]
            vali = ord(stri) - ord('A') + 1
            whole += vali*(26**(size-1-i))
            print(i, stri, vali, whole)
        return whole
# @lc code=end

