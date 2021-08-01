#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def curv(height, i, j):
            return (j-i)*min(height[i], height[j])

        if len(height)<=1: return 0
        if len(height)==2: return curv(height, 0, 1)

        n = len(height)
        dp = [[0]*n for _ in range(n)]

        # dp[i][<=i]=0
        # dp[i][i+1] = cur(i, i+1)
        # dp[i][j] = max(cur(), dp[i][j-1])

        for left in range(n-1):
            for right in range(left, n):
            # for right in range(n):
            #     for left in range(right+1):
                dp[left][right] = max(\
                    curv(height, left, right), \
                    max(dp[left][right-1],
                    dp[left-1][right]))
        for i in range(n):
            print(dp[i])
        return dp[0][n-1]

# @lc code=end

