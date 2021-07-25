#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []:
            return m*n
        row = []
        column = []
        for i in ops:
            row.append(i[0])
            column.append(i[1])
        return min(row) * min(column)

# @lc code=end

