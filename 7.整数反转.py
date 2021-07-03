#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        flag = ''
        if string[0] == '-':
            flag = '-'
            string = string[-1:0:-1]
            x = - int(string)
        else:
            string = string[-1::-1]
            x = int(string)


        return x if -2**31 < x < 2**31 else 0
        
# @lc code=end

