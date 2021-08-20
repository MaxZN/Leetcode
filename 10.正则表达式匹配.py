#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return True
        if not s and len(p)>=1: return False

        m = len(s)+1
        n = len(p)+1
        dp = [[False]*n for _ in range(m)]
        dp[0][0] = True

        for j in range(2, n):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j - 2]

        print(dp[0])
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if p[j - 2] in [s[i - 1], '.']:  # 若 s[i - 1] 可匹配
                        # *n times cannt cal, so get_pre i-1
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]  # '*'匹配多次或0次
                    else:  # 若 s[i - 1] 不可匹配
                        dp[i][j] = dp[i][j - 2]  # '*'只能匹配0次
                elif p[j - 1] in [s[i - 1], '.']:  # 直接匹配
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m-1][n-1]
# @lc code=end

