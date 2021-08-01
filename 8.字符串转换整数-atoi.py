#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        ans, sign, count = None, 1, 0
        for c in s:
            if c == ' ':
                if ans is not None:
                    break
                elif count:
                    return 0
            elif '0' <= c <= '9':
                if ans is None:
                    ans = int(c)
                else:
                    ans = ans * 10 + int(c)
            elif c == '-' or c == '+':
                if ans is not None:
                    break
                count += 1
                if count > 1:
                    return 0
                if c == '-':
                    sign = -1
            else:
                break
        if ans is None:
            return 0
        return min(sign * ans, 2 ** 31 - 1) if sign > 0 else max(sign * ans , -2**31) 

# @lc code=end

