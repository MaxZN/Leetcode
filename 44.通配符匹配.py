#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s) + 1
        n = len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True

        for j in range(1, n):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] == '?' or s[i-1]==p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]

# @lc code=end

