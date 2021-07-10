#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            tmp = [1] * (i + 1)
            for j in range(i + 1):
                if 0 < j < i:
                    tmp[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(tmp)

        return res

# @lc code=end

