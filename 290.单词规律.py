#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(" ")
        z_s = {}
        if len(list_s) == len(pattern):
            n = len(pattern)
        else:
            return False
        for i in range(n):
            if pattern[i] in z_s and z_s[pattern[i]] != list_s[i]:
                return False
            elif pattern[i] not in z_s:
                z_s[pattern[i]] = list_s[i]
        z_p = {}
        for i in range(n):
            if list_s[i] in z_p and z_p[list_s[i]] != pattern[i]:
                return False
            elif list_s[i] not in z_p:
                z_p[list_s[i]] = pattern[i]
        return True

# @lc code=end

