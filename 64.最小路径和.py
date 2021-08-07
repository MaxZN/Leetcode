#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if row==0 and col==0:
                    dp[row][col] = grid[row][col]
                elif row==0:
                    dp[row][col] = dp[row][col-1] + grid[row][col]
                elif col==0:
                    dp[row][col] = dp[row-1][col] + grid[row][col]
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1]) \
                        + grid[row][col]
                    
        return dp[m-1][n-1]
# @lc code=end

