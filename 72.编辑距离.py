#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1, n2+1):
            dp[0][i] = dp[0][i-1] + 1
        for j in range(1, n1+1):
            dp[j][0] = dp[j-1][0] + 1
        
        for i in range(1, n2+1):
            for j in range(1, n1+1):
                if word1[j-1] == word2[i-1]:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    replace = dp[j-1][i-1]
                    remove = dp[j-1][i]
                    add = dp[j][i-1]
                    dp[j][i] = min(replace, remove, add) + 1
        return dp[-1][-1]

# @lc code=end

