#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res+=4
                    if i-1>=0 and grid[i-1][j]==1:
                        res-=2
                    if j-1>=0 and grid[i][j-1]==1:
                        res-=2
        return res

# @lc code=end

