#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        rmlist = ''
        for i in s:
            tmp = i.lower()
            if 'a'<=tmp<='z' or '0'<=tmp<='9':
                rmlist += tmp
        print(rmlist)
        return rmlist == rmlist[::-1]
            
# @lc code=end

