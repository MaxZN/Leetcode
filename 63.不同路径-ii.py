#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                elif row==0 and col==0:
                    dp[row][col] = 1
                elif row==0:
                    dp[row][col] = dp[row][col-1]
                elif col==0:
                    dp[row][col] = dp[row-1][col]
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
                    
        return dp[m-1][n-1]
# @lc code=end

