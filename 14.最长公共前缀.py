#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        strLen = [len(str) for str in strs]
        minLen = min(strLen)
        n = len(strs)
        if minLen == 0:
            return ''
        for i in range(minLen):
            for j in range(1, n):
                if strs[j][i] != strs[j - 1][i]:
                    return strs[0][:i]
        return strs[strLen.index(minLen)]

# @lc code=end

