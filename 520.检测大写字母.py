#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.lower(): return True
        if word[1:] == word[1:].lower(): return True
        if word.upper() == word: return True
        return False
# @lc code=end

