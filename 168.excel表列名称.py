#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber

        res = ""
        while n:
            n -= 1
            tmp = n % 26
            res = chr(ord('A') + tmp ) + res
            n //= 26
        return res


# @lc code=end

