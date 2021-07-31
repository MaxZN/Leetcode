#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mat = [[False] * n]*n
        for i in range(n):
            mat[i][i] = 1
        
        for i in range(n):
            for j in range(n)

# @lc code=end

