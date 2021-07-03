#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if len(s) == 0:
            return 0
        s_list = s.split(' ')
        return len(s_list[-1])
        
# @lc code=end

