#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2:
            return False
        if 'LLL' not in s:
            return True
        return False
# @lc code=end

