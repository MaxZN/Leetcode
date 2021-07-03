#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        rev = string[::-1]
        return rev==string
# @lc code=end

