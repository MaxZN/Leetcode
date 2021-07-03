#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        Hash = {'I':1, 'V':5, 'X':10, \
                'L':50, 'C':100, 'D':500, \
                'M':1000}
        res = 0
        for i,si in enumerate(s):
            if i==len(s)-1:
                res += Hash[si]
            else:
                post = s[i+1]
                if Hash[si] >= Hash[post]:
                    res += Hash[si]
                else:
                    res -= Hash[si]

        return res
# @lc code=end

